import argparse
from typing import Dict, List
import logging

from prettyTables import Table

from ds_helper.ds_helpers import return_tags
from ds_helper.rucio_helper import get_files, lookup_datasets

from .ami_helper import ami_tag_metadata


def find(args):
    """Run the find command

    * Search RUCIO for a wild-card set of samples
    * Filter out datasets that have no files in them
    * Find the release of the last tag in the dataset and dump it all.

    Args:
        args (Dict[str, str]): The arguments from the `argparse` command
    """
    logging.info(f"Looking up datasets matching {args.ds_name}")
    all_datasets = lookup_datasets(args.scope, args.ds_name)
    info: List[Dict[str, str]] = []
    for ds in all_datasets:
        logging.info(f"Getting files list for {ds}")
        files = get_files(args.scope, ds)
        count = sum(1 for _ in files)
        dt = {"Name": ds, "Files": count}
        if count > 0:
            if args.ami:
                tag = return_tags(ds)[-1]
                logging.info(f"Getting AMI metadata for {tag}")
                cache_name = ami_tag_metadata(tag)["cacheName"]
                dt["Cache"] = cache_name
            info.append(dt)

    if len(info) > 0:
        output_table = Table()
        for c in info[0].keys():
            output_table.add_column(c, [f_info[c] for f_info in info])
        print(output_table)


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
    parser.add_argument(
        "--verbose", "-v", action="count", default=0, help="Verbosity level"
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
    cmd_find.add_argument(
        "--ami",
        action=argparse.BooleanOptionalAction,
        help="Allow AMI tag lookup",
        default=True,
    )
    cmd_find.set_defaults(func=find)

    # Parse the input and we are done.
    args = parser.parse_args()

    # Set the logging level
    if args.verbose == 0:
        logging.basicConfig(level=logging.WARNING)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.INFO)
    elif args.verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)

    args.func(args)


if __name__ == "__main__":
    main()
