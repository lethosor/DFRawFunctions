"""
Enables all raw objects in a specified folder
"""

import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--raw', help='The raw folder to modify', required=True)
parser.add_argument('--backup', required=False, default=None,
    help='A folder to copy the raws to before modification (optional)')
args = parser.parse_args()
