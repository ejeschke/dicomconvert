import os
import yaml

meta_home, _ = os.path.split(__file__)
meta_path = os.path.join(meta_home, 'dicom_meta.yml')

# list of attributes available in dicom image
with open(meta_path, 'r') as in_f:
    buf = in_f.read()
dicom_image_description = yaml.safe_load(buf)
dicom_fieldnames = list(dicom_image_description["Description"].values())
