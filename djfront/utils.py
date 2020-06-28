#!/usr/bin/env python3
#                            _                _____
#      /\                   | |       /\     |_   _|
#     /  \     ____   __ _  | |_     /  \      | |
#    / /\ \   |_  /  / _` | | __|   / /\ \     | |
#   / ____ \   / /  | (_| | | |_   / ____ \   _| |_
#  /_/    \_\ /___|  \__,_|  \__| /_/    \_\ |_____|
#
#
import os
from glob import glob
from pathlib import Path

here = os.getcwd()


def get_all_htmls():
    """
    Get all html files in current directory, return None if none of html files found.
    :return: list
    """
    pattern = f"{here}/*.html"
    htmls = glob(pattern)
    return htmls


print(get_all_htmls())
