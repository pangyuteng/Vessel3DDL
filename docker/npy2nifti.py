import os
import sys
import numpy as np
import SimpleITK as sitk

npy_file = sys.argv[1]
img_mhd_file = sys.argv[2]
output_folder = sys.argv[3]

mask = np.load(npy_file)
mask = mask.astype(np.int16)

reader= sitk.ImageFileReader()
reader.SetFileName(img_mhd_file)
img_obj = reader.Execute()
mask_obj = sitk.GetImageFromArray(mask)
mask_obj.SetOrigin((0,0,0))
mask_obj.SetDirection((1,0,0,0,1,0,0,0,1))
mask_obj.SetSpacing((1,1,1))
#mask_obj.CopyInformation(img_obj)

os.makedirs(output_folder,exist_ok=True)
img_nifti_file = os.path.join(output_folder,'image.nii.gz')
mask_nifti_file = os.path.join(output_folder,'mask.nii.gz')

for obj,file_path in [(img_obj,img_nifti_file),(mask_obj,mask_nifti_file)]:
    writer = sitk.ImageFileWriter()
    writer.SetFileName(file_path)
    writer.SetUseCompression(True)
    writer.Execute(obj)

'''
python docker/npy2nifti.py \
    /workdir/Data/Serialized/Output/300iter_24atoms_5bs_1a_5es_100000patches_5ps_20stacks_OutputVolume.npy \
    /workdir/Data/VESSEL12/VESSEL12_ExampleScans/Scans/VESSEL12_21.mhd \
    /workdir/Data/tmp-inference
'''