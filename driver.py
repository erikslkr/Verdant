import argparse

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


if __name__ == "__main__":
    main()
