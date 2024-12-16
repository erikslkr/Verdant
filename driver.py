import argparse
import os

from errors import driver_error, driver_warning
from _version import __version__


def argparser():
    parser = argparse.ArgumentParser(
        prog="verdant",
        description="Compiler for the Verdant programming language",
        add_help=False
    )
    parser.add_argument(
        "source",
        help="Source file (.vd)"
    )
    parser.add_argument(
        "-h", "--help",
        action="store_true",
        help="Show this help message"
    )
    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show version"
    )
    
    return parser


def main():
    parser = argparser()
    args = parser.parse_args()
    
    if args.version:
        print(f"verdant {__version__}")
    if args.help:
        parser.print_help()
        return
    
    if not os.path.exists(args.source):
        driver_error(f"'{args.source}' does not exist")
        # TODO: suggest files with similar names, if possible
        return
    
    if os.path.isdir(args.source):
        driver_error(f"'{args.source}' is a directory")
        # TODO: suggest files with similar names, if possible
        return
    
    if not args.source.endswith(".vd"):
        driver_warning(f"'{args.source}' is not a .vd file")


if __name__ == "__main__":
    main()
