from WORC import IntermediateFacade

datadir = '/home/martijn/Documents/Data/STWStrategyMMD'
label_file = '/home/martijn/Documents/Data/STWStrategyMMD/pinfo.csv'

I = IntermediateFacade('Example_STWStrategyMMD')

I.images_from_this_directory(datadir)
I.segmentations_from_this_directory(datadir,
                                    segmentation_file_name='mask.nii.gz')
I.labels_from_this_file(label_file)
I.predict_labels(['imaginary_label_1'])

I.binary_classification()

I.execute()
