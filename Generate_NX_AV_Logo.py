"""
Exporting the Nxmee/AV logo to whatever size, background, orientation you want using inkscape.

Requires inkscape to be in PATH

Author: Chris Hart
Email: Chris@nxmee.com
Version: 
"""

import argparse
from pathlib import Path
import re

class HexAuth(object):
    # Class for authenticating hex colors are entered in the correct arguments
    def __init__(self):
        self._pattern = re.compile("^#(?:[0-9a-fA-F]{1,2}){3}$")

    def __call__(self, value):
        if not self._pattern.match(value):
            raise argparse.ArgumentTypeError(
                "Invalid hex color entered, plase use format #AABBCC or #ABC"
            )
        return value

def parse_args() -> argparse.Namespace:
    """Parses the script's arguments

    Returns:
        a namespace with the script arguments
    Raises:
        argparse.ArgumentTypeError: If an invalid hex is inputted for either color values

    """
    hex_color = HexAuth()
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-b", "--background", type=hex_color, help="Background color of exported logo/s"
    )
    parser.add_argument(
        "-c",
        "--color",
        type=hex_color,
        default="#000",
        help="Color of the exported logo/s (default: #000)",
    )

    rotations = parser.add_mutually_exclusive_group()

    rotations.add_argument(
        "-r",
        "--rotation",
        type=int,
        default=0,
        help="Custom rotation of the logo (default: 0)",
    )
    rotations.add_argument(
        "-n", "--nxmee", action="store_true", help="Orients the logo to the Nxmee angle"
    )
    rotations.add_argument(
        "-a",
        "--antiviral",
        action="store_true",
        help="Orients the logo to the Antiviral angle",
    )

    parser.add_argument(
        "-p",
        "--prefix",
        default="Logo_",
        help="Prefix for the generated files (default: Logo_)",
    )
    parser.add_argument(
        "-s", "--suffix", default="", help="Suffix for the generated files (default: )"
    )
    parser.add_argument("-f", "--folder", default=str(Path.cwd().joinpath("out")), help="Folder location for the output (default: out)")

    parser.add_argument(
        "sizes", nargs="+", type=int, help="sizes of the logo to be exported"
    )

    args = parser.parse_args()
    return args

def main():
    args = parse_args()

if __name__ == "__main__":
    main()
