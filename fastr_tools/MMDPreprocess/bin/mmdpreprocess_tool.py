#!/usr/bin/env python

# Copyright 2011-2018 Biomedical Imaging Group Rotterdam, Departments of
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

import argparse
from mmdpreprocess import mmdpreprocess


def main():
    parser = argparse.ArgumentParser(description='Feature extraction')
    parser.add_argument('-im_in', '--im_in', metavar='im_in', nargs='+',
                        dest='im_in', type=str, required=True,
                        help='DICOM folder to process')
    parser.add_argument('-im_out', '--im_out', metavar='im_in', dest='im_out',
                        type=str, required=True, nargs='+',
                        help='Image output (ITK Image)')
    parser.add_argument('-seg_out', '--seg_out', metavar='seg_out',
                        dest='seg_out',
                        type=str, required=True, nargs='+',
                        help='Segmentation output (ITK Image)')
    args = parser.parse_args()

    mmdpreprocess(image_in=args.im_in, image_out=args.im_out,
                  segmentation_out=args.seg_out)


if __name__ == '__main__':
    main()
