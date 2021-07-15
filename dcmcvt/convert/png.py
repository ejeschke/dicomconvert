import pydicom as dicom
import cv2
import numpy as np

from dcmcvt.meta.info import dicom_fieldnames


def dicom2png(in_dcm_path, out_png_path):

    ds = dicom.dcmread(path)
    arr = np.array(ds.pixel_array)

    # TODO: add to PNG metadata
    # for field in dicom_fieldnames:
    #     try:
    #         if ds.data_element(field) is not None:
    #             x = str(ds.data_element(field)).replace("'", "")
    #             y = x.find(":")
    #             value = x[y+2:]
    #             # FITS strings have a max size of 68 characters
    #             #hdr['hierarch {}'.format(field)] = value[:40]
    #             hdr[field[:8]] = value[:40]
    #     except Exception as e:
    #         continue
    #     print(field, value)

    cv2.imwrite(out_path, arr.astype(np.uint16))
