from functools import lru_cache
from typing import Dict

import pyAMI.client


@lru_cache(maxsize=100)
def ami_tag_metadata(tag_name: str) -> Dict[str, str]:
    """Return all the tag metadata we can find for a particular tag name.

    Args:
        tag_name (str): The tag name, like

    Returns:
        List[str]: The list of entries in the AMI database for that tag.
    """
    client = pyAMI.client.Client(["atlas-replica", "atlas"])
    resDict = client.execute(f"GetAMITagInfo -amiTag={tag_name}", format="dict_object")
    info = resDict.get_rows()  # type: ignore
    assert len(info) == 2
    tag_info = info[1]
    return tag_info
