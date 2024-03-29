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
import sys

# import src
 
import yaml
from yaml import SafeLoader

from halo import Halo
import time


spinner = Halo(text='Loading', spinner='point')
spinner.start()

time.sleep(3)

spinner.stop()