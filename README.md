# Nxmee/Antiviral Logo Generator
A simple python generator to create .png versions of the 2022 refresh of my Nxmee/Antiviral logo

- [Nxmee/Antiviral Logo Generator](#nxmeeantiviral-logo-generator)
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [Base Use](#base-use)
    - [Arguments](#arguments)

## Requirements
- Inkscape 1.2.1 or above in PATH
- Python 3.4 or above


## Usage

### Base Use
Python Generate_NX_AV_Logo.py size

### Arguments

**Positional arguments:**

  sizes                 sizes of the logo to be exported


**Options:**


  -h, --help            
  
       show the help message and exit


  -b BACKGROUND, --background BACKGROUND


       Background color of exported logo/s

                        
  -c COLOR, --color COLOR


        Color of the exported logo/s (default: #000)


  -r ROTATION, --rotation ROTATION

        Custom rotation of the logo (default: 0)


  -n, --nxmee
  
       Orients the logo to the Nxmee angle


  -a, --antiviral

       Orients the logo to the Antiviral angle


  -p PREFIX, --prefix PREFIX


        Prefix for the generated files (default: Logo_)


  -s SUFFIX, --suffix SUFFIX


        Suffix for the generated files (default: )


  -f FOLDER, --folder FOLDER


        Folder location for the output (default: out)