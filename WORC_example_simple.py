from WORC import IntermediateFacade

# ---------------------------------------------------------------------------
# Input
# ---------------------------------------------------------------------------
# Below are the minimal inputs:
#   - Images
#   - Segmentations
#   - Labels

# Here, we assume you have a folder "datadir", in which there is a folder for each
# patient, where in each folder there is a image.nii.gz and a mask.nii.gz. You
# an change both the folder and filenames accordlingly to your data.

datadir = '/home/martijn/Documents/Data/STWStrategyMMD'
image_file_name = 'image.nii.gz'
segmentation_file_name = 'mask.nii.gz'

# File in which the labels (i.e. outcome you want to predict) is stated
label_file = '/home/martijn/Documents/Data/STWStrategyMMD/pinfo.csv'

# Name of the label you want to predict
label_name = 'imaginary_label_1'

# Determine whether we want to do a coarse quick experiment, or a full lengthy one
coarse = True

# Give your experiment a name
experiment_name = 'Example_STWStrategyMMD'

# ---------------------------------------------------------------------------
# The actual experiment
# ---------------------------------------------------------------------------

# Create a WORC object
I = IntermediateFacade(name)

# Set the input data according to the variables we defined earlier
I.images_from_this_directory(datadir,
                             image_file_name=image_file_name)
I.segmentations_from_this_directory(datadir,
                                    segmentation_file_name=segmentation_file_name)
I.labels_from_this_file(label_file)
I.predict_labels([label_name])

# Use the standard workflow for binary classification
I.binary_classification(coarse=coarse)

# Run the experiment!
I.execute()
