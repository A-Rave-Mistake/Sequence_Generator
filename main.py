# --- GENERAL INFO ---

    #  Sequence generator generates a specified amount of combinations, these combinations can be made from ordered alphabet letters or/and numbers as well as said
    #  characters in random order. The program can also generate results from text files, provided that each "item" in said files is separated by a new line.
    #  The program can be used to generate full names, passwords or user tokens. The program allows for much customization and can be used for various goals.
    #  This file in particular is used only for running the program and activating the GUI classes from menus.py and isn't used much apart from that.

    
# --- LICENSE ---

    # Copyright (C) 2022 Adrian Urbaniak (FancySnacks)

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

    
    
   
# --- SCRIPT BEGINS HERE ---

    
from functions import *
import menus


# References
MainWindow = None
session = None


# Main
if __name__ == "__main__":
    initialize()
