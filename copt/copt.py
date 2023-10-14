#!/usr/bin/env python3

"""
Copyright 2023 Juliandev02

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundationat version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from src import *
from src.colors import *

import os
import sys

from sys import argv

arg_len = len(argv)

package_list = ["sys-base", "sys-base-dev"]

match arg_len > 1 and argv[1]:
    case "help":
        print(help_message)
    
    case "install":
        if not arg_len > 2:
            exit(1)
        
        if not os.path.exists(directories.var_spkg) or not os.path.exists(directories.base_spkg):
            print(f"{RED + BOLD}E: {CRESET}spkg was not found on this system. Please consider installing spkg before using copt!")
            exit(1)
        
        bootstrap_list = argv[2:]
        not_found_packages = [item for item in bootstrap_list if item not in package_list]

        
        if not_found_packages:
            print(f"{RED + BOLD}E: {CRESET}Following packages were not found: {not_found_packages}")
            exit()
            
            
        print(bootstrap_list)
