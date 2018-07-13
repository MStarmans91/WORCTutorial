#!/usr/bin/env python

# Copyright 2017-2018 Biomedical Imaging Group Rotterdam, Departments of
# Medical Informatics and Radiology, Erasmus MC, Rotterdam, The Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import dicom as pydicom
import SimpleITK as sitk
import numpy as np
import random


def mmdpreprocess(image_in, image_out, segmentation_out):
        '''
        Converts input image DICOM folder to output nifti and segmentation.

        Parameters
        ----------
        WIP

        '''
        # Convert input arguments from list to arguments
        if type(image_in) is list:
            image_in = ''.join(image_in)

        if type(image_out) is list:
            image_out = ''.join(image_out)

        if type(segmentation_out) is list:
            segmentation_out = ''.join(segmentation_out)

        # Load the DICOMs from the folder
        image, _ = load_image(image_in)

        # We make a dummy segmentation by simply selecting a cube in the image
        # Note that we use a random volume of either 10 or 20 for half width.
        width = random.choice([10, 20])
        x, y, z = image.shape
        mask = np.zeros(image.shape)
        mask[int(x)/2 - width:int(x)/2 + width,
             int(y)/2 - width:int(y)/2 + width,
             int(z)/2 - width:int(z)/2 + width] = 1

        # Save image and mask
        image = sitk.GetImageFromArray(image)
        mask = sitk.GetImageFromArray(mask)
        sitk.WriteImage(image, image_out)
        sitk.WriteImage(mask, segmentation_out)


def load_image(input_dir):
    '''
    Load DICOMs from input_dir to a single 3D image and make sure axial
    direction is on third axis.
    '''
    dicom_reader = sitk.ImageSeriesReader()
    dicom_file_names = dicom_reader.GetGDCMSeriesFileNames(str(input_dir))
    dicom_reader.SetFileNames(dicom_file_names)
    metadata = pydicom.read_file(dicom_file_names[0])
    dicom_image = dicom_reader.Execute()
    dicom_image = sitk.GetArrayFromImage(dicom_image)

    dicom_image = np.transpose(dicom_image, (2,1,0))
    dicom_image = np.fliplr(np.rot90(dicom_image, 3))
    dicom_image = dicom_image[:, :, ::-1]
    return dicom_image, metadata
