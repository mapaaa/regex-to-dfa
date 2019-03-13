#!/usr/bin/python3

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Tool to transform regex to DFA')
    parser.add_argument('alphabet', type=str, help='Alphabet of REGEX.')
    parser.add_argument('regex', type=str, help='Regular expression.')

    args = parser.parse_args()
    regex = args.regex
    alphabet = args.alphabet


if __name__ == '__main__':
    sys.exit(main());
