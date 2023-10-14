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

import os
import platform

from src.colors import *

version = "1.0.0"

class directories:
    var_spkg    = "/var/lib/spkg/"
    base_spkg   = "/usr/share/spkg/"

help_message = f"""{GREEN}{BOLD}coreOS Package Tool{CRESET} ({version}) {platform.machine()}

{CYAN}{BOLD}Usage:{RESET} copt {GREEN}[Command] {RED}<Argument>

{BOLD}{MAGENTA}-> Package installation, update and removal{CRESET}
    {CYAN}{BOLD}-a{CRESET}      Installs packages
    {CYAN}{BOLD}-d{CRESET}      Removes packages
    {CYAN}{BOLD}-u{CRESET}      Updates packages   
    
{BOLD}{CYAN}-> Package information{CRESET}
    {CYAN}{BOLD}-i{CRESET}      Gives information about packages
    {CYAN}{BOLD}-l{CRESET}      Lists packages according to a certain criterion

{BOLD}{YELLOW}-> Repository management{CRESET}
    {CYAN}{BOLD}-s{CRESET}      Syncs repository

{BOLD}{RED}-> Miscellaneous{CRESET}
    {CYAN}{BOLD}-Ab{CRESET}     About page for copt

{BOLD}{BLUE}-> Bootstrapping{CRESET}
    {CYAN}{BOLD}-Cb{CRESET}     Bootstrapps your system according to the passed arguments"""