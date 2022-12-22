import os
import sys
import numpy as np
import SimpleITK as sitk

npy_file = sys.argv[1]
img_mhd_file = sys.argv[2]
lung_mhd_file = sys.argv[3]
output_folder = sys.argv[4]

mask = np.load(npy_file)
mask = mask.astype(np.float)
print(mask.shape,np.sum(mask))

reader= sitk.ImageFileReader()
reader.SetFileName(img_mhd_file)
img_obj = reader.Execute()

reader= sitk.ImageFileReader()
reader.SetFileName(lung_mhd_file)
lung_obj = reader.Execute()
lung = sitk.GetArrayFromImage(lung_obj)

# npy shape is different from shape from .mhd
# TODO: not sure what's going on here
shift_list = [-25,2,2]
z,x,y = lung.shape
mask = mask[0:z,0:x,0:y]
for idx,shift in enumerate(shift_list):
    mask = np.roll(mask, shift, axis=idx)

print(mask.shape,np.sum(mask))
mask[lung==0]=0
print(mask.shape,np.sum(mask))
mask = mask.astype(np.int16)
mask_obj = sitk.GetImageFromArray(mask)
mask_obj.CopyInformation(img_obj)

os.makedirs(output_folder,exist_ok=True)
img_nifti_file = os.path.join(output_folder,'image.nii.gz')
mask_nifti_file = os.path.join(output_folder,'mask.nii.gz')

for obj,file_path in [(img_obj,img_nifti_file),(mask_obj,mask_nifti_file)]:
    writer = sitk.ImageFileWriter()
    writer.SetFileName(file_path)
    writer.SetUseCompression(True)
    writer.Execute(obj)

'''
# in `conf.py`, `param.volumeToProcess` is set to `Scans/VESSEL12_21.raw`
python docker/npy2nifti.py \
    /workdir/Data/Serialized/Output/300iter_24atoms_5bs_1a_5es_100000patches_5ps_20stacks_OutputVolume.npy \
    /workdir/Data/VESSEL12/VESSEL12_ExampleScans/Scans/VESSEL12_21.mhd \
    /workdir/Data/VESSEL12/VESSEL12_ExampleScans/Lungmasks/VESSEL12_21.mhd \
    /workdir/Data/tmp-inference
'''