#!/usr/bin/python3

import argparse
import sys

from tree import Data


# Adds concatenation symbol '.' in regex for easier parsing.
def add_concatenation(regex, alphabet):
    new_regex = ''
    l = len(regex)
    for i in range(0, l-1):
        new_regex += regex[i]
        # Accepted operators are: '(', ')', '.', '*', '|'
        # so we should add '.' to the following situations:
        # ab -> a.b
        # a( -> a.(
        # )a -> ).a
        # *a -> *.a
        # *( -> *.(
        # )( -> ).(
        if regex[i] in alphabet:
            if regex[i+1] in alphabet:
                new_regex += '.'
            elif regex[i+1] == '(':
                new_regex += '.'
        elif regex[i] == ')':
            if regex[i+1] in alphabet:
                new_regex += '.'
            elif regex[i+1] == '(':
                new_regex += '.'
        elif regex[i] == '*':
            if regex[i+1] in alphabet:
                new_regex += '.'
            elif regex[i+1] == '(':
                new_regex += '.'
    
    new_regex += regex[l-1];
    return new_regex



def make_expression_tree(regex, alphabet):
    operators = ['*', '|', '.']

    regex = add_concatenation(regex, alphabet)
    # TODO transform regex into expression tree 
    #stack = [regex[0]]
    #l = len(regex)
    #for i in range(1, l):
        #if regex[i] in alphabet:
            


def main():
    parser = argparse.ArgumentParser(description='Tool to transform regex to DFA')
    parser.add_argument('alphabet', type=str, help='Alphabet of REGEX.')
    parser.add_argument('regex', type=str, help='Regular expression.')

    args = parser.parse_args()
    regex = args.regex
    alphabet = args.alphabet

    regex = '(' + regex + ')#'  # mark the end of the expression
    tree = make_expression_tree(regex, alphabet)


if __name__ == '__main__':
    sys.exit(main());
