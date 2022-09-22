"""
Parse commandline options with argparse.
"""

import argparse

parser = argparse.ArgumentParser(description='process data')
parser.add_argument(
    '-i',
    '--input',
    help='input file name',
    default='in.txt')
parser.add_argument(
    '-o',
    '--output',
    help='output file name',
    default='out.txt')

args = parser.parse_args()

print(f'Using input file: {args.input}')
print(f'Using output file: {args.output}')
