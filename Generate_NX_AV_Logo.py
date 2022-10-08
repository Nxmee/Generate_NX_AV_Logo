"""
Exporting the Nxmee/AV logo to whatever size, background, orientation you want using inkscape.

Requires inkscape to be in PATH

Author: Chris Hart
Email: Chris@nxmee.com
Version: 
"""

import argparse
from pathlib import Path, PurePath
import re
import tempfile

BASE_LOGO = [
    '<svg version="1.1" viewBox="0 0 512 512" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">',
    '   <rect width="512" height="512" fill="{bg_fill}"/>',
    '   <g transform="rotate({rotation},256,256)" fill="none" stroke="{logo_stroke}">',
    '       <g stroke-width="55">',
    '           <path d="m221.38 182.49 220.94 220.94"/>',
    '           <path d="m236.56 452.55 249.44-249.44"/>',
    '           <path transform="rotate(195 243.19 261.31)" d="m317.08 483.96-122.16-455.92"/>',
    '           <path d="m21.904 265.8 199.48-199.48"/>',
    "       </g>"
    '       <path d="m492 256a236 236 0 0 1-236 236 236 236 0 0 1-236-236 236 236 0 0 1 236-236 236 236 0 0 1 236 236z" stroke-width="40"/>',
    "   </g>",
    "</svg>",
]

PRESET_ROTATIONS = {"nxmee": 335, "antiviral": 160}

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

def create_temp_file(args: argparse.Namespace) -> PurePath:
    """Creates the SVG file to convert

    This function uses the passed in arguments to construct a temporary SVG file
    with the correct orientation, background and logo colors

    Args:
        args: the argument namespace from parse_args()
    
    Returns:
        PurePath representation of where the SVG is stored

    """

    logo_data = BASE_LOGO

    # Remove background if not specified
    if not args.background:
        logo_data.pop(1)

    # Getting logo rotation
    for preset in PRESET_ROTATIONS.keys():
        if preset in args:
            rotation = PRESET_ROTATIONS[preset]
            break
    else:
        rotation = args.rotation

    style = {
        "bg_fill": args.background,
        "rotation": str(rotation),
        "logo_stroke": args.color,
    }
    logo_data_formatted = []
    for line in logo_data:
        logo_data_formatted.append(line.format(**style))

    temp_dir = tempfile.gettempdir()
    temp_path = PurePath(temp_dir)
    temp_path = temp_path.joinpath("temp_image.svg")

    with open(str(temp_path), "w") as temp_writer:
        temp_writer.writelines(logo_data_formatted)

    return temp_path

def main():
    args = parse_args()
    temp_location = create_temp_file(args)

if __name__ == "__main__":
    main()
