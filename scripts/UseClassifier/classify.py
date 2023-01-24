import os
import sys
import time
import argparse
import SimpleITK as sitk
import numpy as np
from UseClassifier import (
    config,
    LoadClassifier,
    LoadVolume,
    Padd,
    LoadDictionary,
    Divide,
    divideIntoBlocks,
    ApplyAtoms,
    connectAllBlocks,
    SerializeOutput,
)

def imread(fpath):
    reader= sitk.ImageFileReader()
    reader.SetFileName(fpath)
    return reader.Execute()

def imwrite(fpath,img_obj,use_compression=True):
    writer = sitk.ImageFileWriter()    
    writer.SetFileName(fpath)
    writer.SetUseCompression(use_compression)
    writer.Execute(img_obj)
 
#
# assumption, adult lung volume similar, voxel size similar, thus resample all volumes to 512^3
# this is probably "okay" assuming slice num to be 400 to 600?
# or should we actually check vessel12 spacing?
#
# TODO: alternative approach, probably better, resize to desired out_spacing, then if ncessary, pad.
#
# ref. https://gist.github.com/mrajchl/ccbd5ed12eb68e0c1afc5da116af614a
def resample_img(itk_image, out_size=[512,512,512], is_label=False):

    original_spacing = itk_image.GetSpacing()
    original_size = itk_image.GetSize()

    out_spacing = [
        original_size[0] * (original_spacing[0] / out_size[0]),
        original_size[1] * (original_spacing[1] / out_size[1]),
        original_size[2] * (original_spacing[2] / out_size[2])]

    resample = sitk.ResampleImageFilter()
    resample.SetOutputSpacing(out_spacing)
    resample.SetSize(out_size)
    resample.SetOutputDirection(itk_image.GetDirection())
    resample.SetOutputOrigin(itk_image.GetOrigin())
    resample.SetTransform(sitk.Transform())
    resample.SetDefaultPixelValue(itk_image.GetPixelIDValue())

    if is_label:
        resample.SetInterpolator(sitk.sitkNearestNeighbor)
    else:
        resample.SetInterpolator(sitk.sitkBSpline)

    return resample.Execute(itk_image)

#
# entry point for vessel seg using images outside vessel12 dataset.
# logic adapted from UseClassifier.py
#
def main(input_file,output_file):
    
    param = config.read_parameters()

    scale = param.clfS    
    inDict = param.dictionaryName+'.pkl'
    inClass= param.clf2use+'_'+param.dictionaryName

    C = LoadClassifier(param.path2classifier,inClass)
    
    img_obj = imread(input_file)
    resampled_obj = resample_img(img_obj)
    V = sitk.GetArrayFromImage(resampled_obj)
    V = Padd(V)
    D = LoadDictionary(param.path2dicts,inDict)

    print ('start')
    t0=time.time()
    window = 8
    Lv,Rv=Divide(512,128,window)
    NV = divideIntoBlocks(V,Lv,Rv)
    Out = []
    for i in range(len(NV)):
        P=NV[i]
        P=P.astype('float32')
        O=ApplyAtoms(P,D,scale)
        shp = np.shape(P)
        O = O.reshape(scale*param.numOfAtoms,shp[0]*shp[1]*shp[2])
        O = O.T
        y_pred = C.predict(O)
        Out.append(y_pred.reshape(shp[0],shp[1],shp[2]))
    ####
    O=connectAllBlocks(Out,(512,512,512),window)

    # shape of O is 514^2
    mask=O[0:512,0:512,0:512]
    shift = [2,2,1] # ?
    for idx in range(3):
        mask = np.roll(mask, shift[idx], axis=idx)
    mask_obj = sitk.GetImageFromArray(mask)
    mask_obj.CopyInformation(resampled_obj)
    mask_obj = resample_img(mask_obj, out_size=img_obj.GetSize(), is_label=True)
    imwrite(output_file,mask_obj)
    print(time.time()-t0)
    print("Done")

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',help='input .nii.gz file path')
    parser.add_argument('output_file',help='output .nii.gz file path')
    args = parser.parse_args()

    main(args.input_file,args.output_file)

