from typing import List


def return_tags(ds_name: str) -> List[str]:
    """Returns a list of tag names for the given dataset

    Args:
        ds_name (str): The dataset name

    Returns:
        List[str]: List of the tags, in order they are found in the dataset.
    """
    tag_list = ds_name.split(".")[-1]
    tags = tag_list.split("_")
    return tags
