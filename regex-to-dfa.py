#!/usr/bin/python3

import argparse
import sys

from tree import Data
from tree import Node


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
            elif regex[i+1] == '#':
                new_regex += '.'
        elif regex[i] == '*':
            if regex[i+1] in alphabet:
                new_regex += '.'
            elif regex[i+1] == '(':
                new_regex += '.'
    
    new_regex += regex[l-1];
    return new_regex


def do_operation(op):
    if op == '|' or op == '.':
        # binary operators
        right = stack_nodes.pop()
        left = stack_nodes.pop()

        root = Node(left, right)
        root.data = Data(operator=op)
        stack_nodes.append(root)
    elif operator == '*':
        # kleene iteration
        child = stack_nodes.pop()

        root = Node(child)
        stack_nodes.append(root)
    else:
        error('Unknown operator!')


def make_expression_tree(regex, alphabet):
    k = 0
    operators = ['*', '|', '.']

    regex = add_concatenation(regex, alphabet)
    stack = [regex[0]]
    global stack_nodes
    stack_nodes = []
    l = len(regex)
    for i in range(1, l):
        if regex[i] == '(':
            stack.append('(')
        if regex[i] == ')':
            while len(stack) > 0:
                top = stack.pop()
                if top == '(':
                    break
                do_operation(top);
        if regex[i] in alphabet or regex[i] == '#':
            k += 1
            node = Node();
            node.data = Data(operand=regex[i], label=k)
            stack_nodes.append(node)
        if regex[i] in operators:
            node = Node();
            node.data = Data(operator=regex[i])
            stack_nodes.append(node)

    while len(stack) > 0:
        top = stack.pop()
        do_operation(top)

    tree = stack_nodes.pop();
    return tree

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
