# Using BasicWORC, this tutorials shows how to use your own features. 
# For more information on how to save your features correctly and 
# configure WORC for using your own features, see
# https://worc.readthedocs.io/en/development/static/faq.html#can-i-use-my-own-features-instead-of-the-standard-worc-features.

# import neccesary packages
from WORC import BasicWORC
import os

# These packages are only used in analysing the results
import pandas as pd
import json
import fastr
import glob

# Define the folder this script is in, so we can easily find the example data
script_path = os.path.dirname(os.path.abspath(__file__))

# Determine whether you would like to use WORC for binary_classification,
# multiclass_classification or regression
modus = 'binary_classification'


def main():
    """Execute WORC Tutorial experiment."""
    print(f"Running in folder: {script_path}.")
    # -------------------------------------------------------------------------------
    # This tutorial will first largely follow the same steps as the BasicWORC tutorial.
    # -------------------------------------------------------------------------------
    
    # File in which the labels (i.e. outcome you want to predict) is stated
    # Again, change this accordingly if you use your own data.
    data_path = os.path.join(os.path.dirname(script_path), 'Data')
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
    experiment_name = 'Example_STWStrategyHN_BasicWORC_OwnFeatures'

    # Instead of the default tempdir, let's but the temporary output in a subfolder
    # in the same folder as this script
    tmpdir = os.path.join(script_path, 'WORC_' + experiment_name)
    print(f"Temporary folder: {tmpdir}.")

    # ---------------------------------------------------------------------------
    # The actual experiment: here we will use BasicWORC
    # ---------------------------------------------------------------------------

    # Create a BasicWORC object
    experiment = BasicWORC(experiment_name)

    # Provide feature files to WORC. For this experiment, we demonstrate the the workflow
    # of not providing images and segmentations but features using the output from the
    # WORCTutorialBasic.
    
    # Locate output folder of previous experiment
    outputfolder = fastr.config.mounts['output']
    experiment_folder = os.path.join(outputfolder, 'WORC_Example_STWStrategyHN')

    # find feature files: change accordingly based on your setup
    features = glob.glob(os.path.join(experiment_folder,
                                      'Features',
                                      'features*predict*.hdf5'))

    features = {f"{featurefile[-13:-5]}": featurefile for featurefile in features}
    
    # We now append this dictionary to the images_train object. The
    # features_from_this_directory function from SimpleWORC also appends to this object.
    experiment.features_train.append(features)
    
    # Note: if you provide images, segmentations, and features, WORC will only use the images and 
    # segmentations in parts of the evaluation setup if you added that. WORC will not extract
    # new features from the images.

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
    experiment.set_multicore_execution()
    experiment.add_evaluation()
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

    # Read the overall peformance
    performance_file = os.path.join(experiment_folder, 'performance_all_0.json')
    if not os.path.exists(performance_file):
        print(f'No performance file {performance_file} found: your network has failed.')

    with open(performance_file, 'r') as fp:
        performance = json.load(fp)

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
