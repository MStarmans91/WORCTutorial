# Welcome to the tutorial of WORC: a Workflow for Optimal Radiomics
# Classification! # This tutorial interacts with WORC through BasicWORC,
# which is based on SimpleWORC (SimpleWORC is the parent class of BasicWORC)
# but provides additional functionality. For # first time use, we recommend
# the WORCTutorialSimple using SimpleWORC, where we also
# mention tips and tricks also valid for BasicWORC.

# import neccesary packages
from WORC import BasicWORC
import os

# These packages are only used in analysing the results
import pandas as pd
import json
import fastr
import glob

# If you don't want to use your own data, we use the following example set,
# see also the next code block in this example.
from WORC.exampledata.datadownloader import download_HeadAndNeck

# Define the folder this script is in, so we can easily find the example data
script_path = os.path.dirname(os.path.abspath(__file__))

# Determine whether you would like to use WORC for binary_classification,
# multiclass_classification or regression
modus = 'binary_classification'


def main():
    """Execute WORC Tutorial experiment."""
    print(f"Running in folder: {script_path}.")
    # ---------------------------------------------------------------------------
    # Input: Same as the SimpleWORC tutorial
    # ---------------------------------------------------------------------------
    
    # -------------------------------------------------------------------------------
    # This part will first largely follow the same steps as the SimpleWORC tutorial.
    # -------------------------------------------------------------------------------
    
    # Download a subset of 20 patients in this folder. You can change these if you want.
    nsubjects = 20  # use "all" to download all patients
    data_path = os.path.join(script_path, 'Data')
    download_HeadAndNeck(datafolder=data_path, nsubjects=nsubjects)

    # Identify our data structure: change the fields below accordingly
    # if you use your own data.
    imagedatadir = os.path.join(data_path, 'stwstrategyhn1')
    image_file_name = 'image.nii.gz'
    segmentation_file_name = 'mask.nii.gz'

    # File in which the labels (i.e. outcome you want to predict) is stated
    # Again, change this accordingly if you use your own data.
    label_file = os.path.join(data_path, 'Examplefiles', 'pinfo_HN.csv')

    # Name of the label you want to predict
    if modus == 'binary_classification':
        # Classification: predict a binary (0 or 1) label
        label_name = ['imaginary_label_1']

    elif modus == 'regression':
        # Regression: predict a continuous label
        label_name = ['Age']

    elif modus == 'multiclass_classification':
        # Multiclass classification: predict several mutually exclusive binaru labels together
        label_name = ['imaginary_label_1', 'complement_label_1']

    # Determine whether we want to do a coarse quick experiment, or a full lengthy
    # one. Again, change this accordingly if you use your own data.
    coarse = True

    # Give your experiment a name
    experiment_name = 'Example_STWStrategyHN_BasicWORC'

    # Instead of the default tempdir, let's but the temporary output in a subfolder
    # in the same folder as this script
    tmpdir = os.path.join(script_path, 'WORC_' + experiment_name)
    print(f"Temporary folder: {tmpdir}.")

    # ---------------------------------------------------------------------------
    # The actual experiment: here we will use BasicWORC
    # ---------------------------------------------------------------------------

    # Create a BasicWORC object
    experiment = BasicWORC(experiment_name)

    # We could still use the ..._from_this_directory SimpleWORC functions, but for
    # this tutorial we will instead directly provide the data to BasicWORC ourselves.
    # To this end, we need to create dictionaties, where the keys will be the sample
    # names (e.g. patient ID) and the values the filenames. The keys are used
    # to match segmentations to images, and match the files to the IDs provides in your
    # label file, so make sure everything corresponds.
    
    # Get the image files and convert to dictionary with patient names as keys
    images = glob.glob(os.path.join(imagedatadir, "*", image_file_name))
    images = {f"{os.path.basename(os.path.dirname(image))}_0": image for image in images}
    
    # We now append this dictionary to the images_train object. The
    # images_from_this_directory function from SimpleWORC also appends to this object.
    experiment.images_train.append(images)
    
    # We do the same with the segmentations
    segmentations = glob.glob(os.path.join(imagedatadir, "*", segmentation_file_name))
    segmentations = {f"{os.path.basename(os.path.dirname(segmentation))}_0": segmentation for segmentation in segmentations} 
    experiment.segmentations_train.append(segmentations)
    
    # There are various other objects you can interact with, see https://worc.readthedocs.io/en/latest/static/user_manual.html#attributes-sources
    # for an overview and the function of each attribute.
    
    # Note: You can keep appending dictionaries to these objects here if you want to
    # use multiple images per patient, e.g. a T1 MRI and a T2 MRI. You should
    # provide matching segmentations for each of the images, as WORC extracts the features
    # per image-segmentation set. Except when you want to
    # use special workflows, e.g. use image registration, see the WORC readthedocs.

    # The rest remains the same as in SimpleWORC
    experiment.labels_from_this_file(label_file)
    experiment.predict_labels(label_name)

    # Set the types of images WORC has to process. Used in fingerprinting
    # Valid quantitative types are ['CT', 'PET', 'Thermography', 'ADC']
    # Valid qualitative types are ['MRI', 'DWI', 'US']
    experiment.set_image_types(['CT'])

    # Use the standard workflow for your specific modus
    if modus == 'binary_classification':
        experiment.binary_classification(coarse=coarse)
    elif modus == 'regression':
        experiment.regression(coarse=coarse)
    elif modus == 'multiclass_classification':
        experiment.multiclass_classification(coarse=coarse)

    # Set the temporary directory
    experiment.set_tmpdir(tmpdir)
    
    # Run the experiment!
    experiment.execute()

    # ---------------------------------------------------------------------------
    # Analysis of results
    # ---------------------------------------------------------------------------

    # There are two main outputs: the features for each patient/object, and the overall
    # performance. These are stored as .hdf5 and .json files, respectively. By
    # default, they are saved in the so-called "fastr output mount", in a subfolder
    # named after your experiment name.

    # Locate output folder
    outputfolder = fastr.config.mounts['output']
    experiment_folder = os.path.join(outputfolder, 'WORC_' + experiment_name)

    print(f"Your output is stored in {experiment_folder}.")

    # Read the features for the first patient
    # NOTE: we use the glob package for scanning a folder to find specific files
    feature_files = glob.glob(os.path.join(experiment_folder,
                                           'Features',
                                           'features_*.hdf5'))

    if len(feature_files) == 0:
        raise ValueError('No feature files found: your network has failed.')

    feature_files.sort()
    featurefile_p1 = feature_files[0]
    features_p1 = pd.read_hdf(featurefile_p1)

    # Read the overall peformance
    performance_file = os.path.join(experiment_folder, 'performance_all_0.json')
    if not os.path.exists(performance_file):
        raise ValueError(f'No performance file {performance_file} found: your network has failed.')

    with open(performance_file, 'r') as fp:
        performance = json.load(fp)

    # Print the feature values and names
    print("Feature values from first patient:")
    for v, l in zip(features_p1.feature_values, features_p1.feature_labels):
        print(f"\t {l} : {v}.")

    # Print the output performance
    print("\n Performance:")
    stats = performance['Statistics']
    for k, v in stats.items():
        print(f"\t {k} {v}.")

    # NOTE: the performance is probably horrible, which is expected as we ran
    # the experiment on coarse settings. These settings are recommended to only
    # use for testing: see also below.
    

if __name__ == '__main__':
    main()
