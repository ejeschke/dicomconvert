import pydicom as dicom
from astropy.io import fits
from astropy.table import Table
import numpy as np

from ..meta.info import dicom_fieldnames


def dicom2fits(in_dcm_path, out_fits_path):

    ds = dicom.dcmread(in_dcm_path)
    arr = np.array(ds.pixel_array)

    hdu = fits.PrimaryHDU(arr)
    hdr = hdu.header

    rows = []
    for field in dicom_fieldnames:
        try:
            if ds.data_element(field) is not None:
                x = str(ds.data_element(field)).replace("'", "")
                y = x.find(":")
                value = x[y+2:]
                # FITS strings have a max size of 68 characters
                hdr['hierarch {}'.format(field)] = value[:40]
                rows.append(dict(key=field, value=value))
        except Exception as e:
            continue

    # write the meta-data also out as a table in a second HDU
    # there shouldn't be an practical limit on this info
    tbl = Table(rows=rows)
    tbl.meta['comments'] = ["Written by dicom2fits"]
    metadata = fits.BinTableHDU(data=tbl)

    hdu_l = fits.HDUList([hdu, metadata])

    hdu_l.writeto(out_fits_path)
