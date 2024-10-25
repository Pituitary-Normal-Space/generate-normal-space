"""
Python script containing functions the main script uses to obtain and manipulate MRI data.
"""

# Standard library imports
import os

# Third party imports
import pandas as pd

# Local application imports
from subject import Subject
from const import (
    PATH_TO_DATA,
    SUFFIX_SUBJECT_ID,
    UNPROCESSED_DATA,
    T1_DATA,
    T1_FILE_NAME_SUFFIX,
    T2_DATA,
    T2_FILE_NAME_SUFFIX,
)


def create_subject_list(key_df: pd.DataFrame, data_path: str = PATH_TO_DATA) -> list:
    """
    Function to create a list of subject IDs from the data path.

    :param key_df: A pandas DataFrame containing the subject map.
    :param healthy: A boolean to indicate the dataset contains patient's with undiseased pituitary glands. Default is True.
    :param data_path: Path to the data directory.

    :return: A list of subject IDs.
    """
    subject_list = []
    for folder_name in os.listdir(data_path):
        # Check if this is a directory
        if not os.path.isdir(os.path.join(data_path, folder_name)):
            continue
        # Extract subject ID from folder name
        subject_id = folder_name.split(SUFFIX_SUBJECT_ID)[0]
        # Extract T1 and T2 paths
        t1_path = os.path.join(
            data_path,
            folder_name,
            subject_id,
            UNPROCESSED_DATA,
            T1_DATA,
            f"{subject_id}{T1_FILE_NAME_SUFFIX}",
        )
        t2_path = os.path.join(
            data_path,
            folder_name,
            subject_id,
            UNPROCESSED_DATA,
            T2_DATA,
            f"{subject_id}{T2_FILE_NAME_SUFFIX}",
        )
        # Use the subject map csv in the data_path directory to get details on this subject
        subject_details = key_df[key_df["Subject"] == int(subject_id)]
        # Check that the subject details are in the subject map
        if subject_details.empty:
            raise (
                f"Subject {subject_id} details not found in subject map. Please ensure all subjects have details in the subject map."
            )
        # Get gender and age of the subject
        sex = subject_details["Gender"].values[0]
        age = subject_details["Age"].values[0]

        # Create a subject object
        subject = Subject(
            subject_id=subject_id,
            age=age,
            sex=sex,
            t1_path=t1_path,
            t2_path=t2_path,
        )

        # Append the subject object to the list
        subject_list.append(subject)

    return subject_list