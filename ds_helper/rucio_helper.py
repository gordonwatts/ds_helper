from typing import Generator
import rucio.client


__rucio_client = rucio.client.Client()


def lookup_datasets(scope: str, search_string: str) -> Generator[str, None, None]:
    """Creates the search for rucio, which returns a generator
    that the caller can iterate over, each one getting a new dataset.

    Args:
        scope (str): The RUCIO scope
        search_string (str): The RUCIO search string

    Returns:
        Generator: Generator that returns the found datasets.
    """
    results = __rucio_client.list_dids(
        scope, {"name": f"{scope}.{search_string}"}, did_type="container"
    )
    return results


def get_files(scope: str, ds_name: str) -> Generator[str, None, None]:
    """Returns a generator that returns the list of files attached to this dataset.

    Args:
        ds_name (str): Fully qualified name of the dataset.

    Yields:
        Generator[str]: Listing of the result files
    """
    return __rucio_client.list_files(scope, ds_name)
