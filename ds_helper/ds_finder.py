from ami_helper import ami_tag_metadata
from ds_helper.ds_helpers import return_tags

import argparse

from ds_helper.rucio_helper import get_files, lookup_datasets


def find(args):
    """Run the find command

    * Search RUCIO for a wild-card set of samples
    * Filter out datasets that have no files in them
    * Find the release of the last tag in the dataset and dump it all.

    Args:
        args (Dict[str, str]): The arguments from the `argparse` command
    """
    all_datasets = lookup_datasets(args.scope, args.ds_name)
    for ds in all_datasets:
        files = get_files(args.scope, ds)
        count = sum(1 for _ in files)
        if count > 0:
            tag = return_tags(ds)[-1]
            cache_name = ami_tag_metadata(tag)["cacheName"]
            print(count, cache_name, ds)


def main():
    """Run the command ds_finder. For help, see arguments."""
    # Build the argument parser
    parser = argparse.ArgumentParser(
        prog="ds_finder",
        description="Interact with rucio and AMI to find datasets and look up metadata",
    )
    parser.add_argument(
        "--scope", help="The RUCIO scope of the dataset", default="mc16_13TeV"
    )
    subparsers = parser.add_subparsers(title="Commands")

    # find command - search for datasets matching a pattern that still have files.
    #                Print out the release, files, and ds name.
    cmd_find = subparsers.add_parser(
        "find", help="Find datasets by pattern match that have files"
    )
    cmd_find.add_argument(
        "ds_name", type=str, help="Dataset name, with standard rucio wildcards"
    )
    cmd_find.set_defaults(func=find)

    # Parse the input and we are done.
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
