import os

# Paths for data from human connectome project
# Folders
PATH_TO_UNPROCESSED_DATA = "unprocessed"
PATH_TO_PROCESSED_DATA = "processed"
SUFFIX_SUBJECT_ID = "_3T_Structural_unproc"
UNPROCESSED_DATA = os.path.join("unprocessed", "3T")
T1_DATA = "T1w_MPR1"
T2_DATA = "T2w_SPC1"
# MRI files
T1_FILE_NAME_SUFFIX = "_3T_T1w_MPR1.nii.gz"
T2_FILE_NAME_SUFFIX = "_3T_T2w_SPC1.nii.gz"
# Key map name for subject details
KEY_MAP_NAME = "subject_map.csv"

# Path to FSL resources
MNI_TEMPLATE = "/Users/charbelmarche/fsl/data/standard/MNI152_T1_1mm.nii.gz"
