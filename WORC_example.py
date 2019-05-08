import WORC
import fastr
import glob
import os

# NOTE: This example is just to condense the content of the WORCTutorial
# Jupyter notebook to a script you can use.

home = os.path.expanduser('~')

# Create network and use simplest plugin for execution.
network = WORC.WORC('example')
network.fastr_plugin = 'LinearExecution'

# Below are the minimal inputs:
#   - Images
#   - Segmentations
#   - Labels
# Instead of images and segmenations you can also use features.

# Below, we are going to tell WORC where your files for these inputs are locatedself.
# Here, we assume you have a folder $HOME/Documents/Data/StrategyMMD
# (or with \\ path separators on Windows), in which there is a folder for each
# patient, where in each folder there is a image.nii.gz and a mask.nii.gz

# You may need to change these to your files, see also the https://worc.readthedocs.io/en/latest/
# on how to do so.

# Search for the files
image_sources = glob.glob(os.path.join(home, 'Documents', 'Data', 'STWStrategyMMD', '*', 'image.nii.gz'))
segmentation_sources = glob.glob(os.path.join(home, 'Documents', 'Data', 'STWStrategyMMD', '*', 'mask.nii.gz'))

# Create a dictionary where the keys are the patient names, so they can be matched with the labels
image_sources = {os.path.basename(os.path.dirname(i)): i for i in image_sources}
segmentation_sources = {os.path.basename(os.path.dirname(i)): i for i in segmentation_sources}

# Append to the network
network.images_train.append(image_sources)
network.segmentations_train.append(segmentation_sources)

# We assume the labels file is in the same data folder as your patient folders.
pinfo_file = os.path.join(home, 'Documents', 'Data', 'STWStrategyMMD', 'pinfo.txt')
network.labels_train.append(pinfo_file)

# WORC passes a config.ini file to all nodes which contains all parameters.
# You can get the default configuration with the defaultconfig function
config = network.defaultconfig()

# This configparser object can be directly supplied to wROC: it will save
# it to a .ini file. You can interact with it as a dictionary and change fields.
# See the Github Wiki for all available fields and their explanation.
config['SampleProcessing']['SMOTE'] = 'False'
config['CrossValidation']['N_iterations'] = '5'
config['Labels']['label_names'] = 'imaginary_label_1'
config['HyperOptimization']['test_size'] = '0.3'
network.fastr_plugin = 'LinearExecution'

# Add the configuration to the network.
network.configs.append(config)

# Build the network: the returned network.network object is a FASTR network.
network.build()

# Convert your appended sources to actual sources in the network.
network.set()

# Execute the network
network.execute()
