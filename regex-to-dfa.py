#!/usr/bin/python3

import argparse
import sys

from dfa import Dfa
from dfa import State
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
        # )# -> ).#
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

        global cnt_nodes
        cnt_nodes = cnt_nodes + 1
        root = Node(left, right)
        root.data = Data(operator=op, ind=cnt_nodes)
        stack_nodes.append(root)
    elif op == '*':
        # kleene iteration
        child = stack_nodes.pop()

        cnt_nodes += 1
        root = Node(child)
        root.data = Data(operator=op, ind=cnt_nodes)
        stack_nodes.append(root)
    else:
        raise ValueError('Unknown operator: ' + str(op))


def priority(op):
    if op == '|':
        return 1
    elif op == '.':
        return 2
    elif op == '*':
        return 3
    else:
        raise ValueError('Unknown operator: ' + str(op))


def make_expression_tree(regex, alphabet):
    k = 0
    global cnt_nodes
    cnt_nodes = 0
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
            cnt_nodes += 1
            node = Node();
            node.data = Data(operand=regex[i], label=k, ind=cnt_nodes)
            stack_nodes.append(node)
        if regex[i] in operators:
            while len(stack) > 0:
                top = stack.pop();
                if top != '(' and priority(top) >= priority(regex[i]):
                    do_operation(top)
                else:
                    stack.append(top)
                    break
            stack.append(regex[i])

    while len(stack) > 0:
        top = stack.pop()
        do_operation(top)

    return (stack_nodes.pop(), k, cnt_nodes)


def compute_functions(node):
    if node.is_leaf() == True:
        node.data.nullable = False
        node.data.first_pos.append(node.data.label)
        node.data.last_pos.append(node.data.label)
        return

    left = node.left
    right = node.right

    if left != None:
        compute_functions(node.left)

    if right != None:
        compute_functions(node.right)

    op = node.get_operator()
    if op == '|':
        node.data.nullable = False
        if left != None:
            node.data.nullable = node.data.nullable or left.get_nullable()
            node.data.first_pos += left.get_first_pos()
            node.data.last_pos += left.get_last_pos()
        if right != None:
            node.data.nullable = node.data.nullable or right.get_nullable()
            node.data.first_pos += right.get_first_pos()
            node.data.last_pos += right.get_last_pos()

    elif op == '.':
        node.data.nullable = True
        if left != None:
            node.data.nullable = node.data.nullable and left.get_nullable()
            if left.get_nullable == True:
                node.data.first_pos += left.get_first_pos()
                node.data.first_pos += right.get_first_pos()
            else:
                node.data.first_pos += left.get_first_pos()
        if right != None:
            node.data.nullable = node.data.nullable and right.get_nullable()
            if right.get_nullable == True:
                node.data.last_pos += left.get_first_pos()
                node.data.last_pos += right.get_first_pos()
            else:
                node.data.last_pos += right.get_last_pos()

    elif op == '*':
        node.data.nullable = 'True'
        node.data.first_pos += left.get_first_pos()
        node.data.last_pos += left.get_last_pos()

    else:
        raise ValueError('Unknown operator: ' + str(op))


def compute_follow_pos(node):
    if node.is_leaf() == True:
        leaf[node.data.label] = node.data.operand
        return

    left = node.left
    right = node.right
    op = node.get_operator()
    if op == '.':
        last_pos_c1 = left.get_last_pos()
        first_pos_c2 = right.get_first_pos()
        for i in range(0, len(last_pos_c1)):
            follow_pos[last_pos_c1[i]] += first_pos_c2
    elif op == '*':
        last_pos_c = left.get_last_pos()
        first_pos_c = left.get_first_pos()
        for i in range(0, len(last_pos_c)):
            follow_pos[last_pos_c[i]] += first_pos_c

    if left != None:
        compute_follow_pos(left)
    if right != None:
        compute_follow_pos(right)


def main():
    parser = argparse.ArgumentParser(description='Tool to transform regex to DFA')
    parser.add_argument('alphabet', type=str, help='Alphabet of REGEX.')
    parser.add_argument('regex', type=str, help='Regular expression.')

    args = parser.parse_args()
    regex = args.regex
    alphabet = args.alphabet

    regex = '(' + regex + ')#'  # mark the end of the expression
    (tree, k, cnt_nodes) = make_expression_tree(regex, alphabet)

    global follow_pos
    follow_pos = [[]] * (k + 1)
    global leaf
    leaf = [0] * (k + 1)

    compute_functions(tree)
    compute_follow_pos(tree)

    # Q, sigma, delta, q0, F
    dfa = Dfa(sigma=alphabet)
    is_final = False
    if cnt_nodes in tree.get_first_pos():
        is_final = True
    dfa.q0 = dfa.new_state(tree.get_first_pos(), is_final)
    p = 0 
    u = 0
    while p <= u:
        for ch in alphabet:
            all_follow_pos = []
            for x in dfa.get_pos(p):
                if leaf[x] == ch:
                    all_follow_pos += follow_pos[x]
            if len(all_follow_pos) != 0 and dfa.is_state_already(all_follow_pos) == False:
                if_final = False
                if cnt_nodes in all_follow_pos:
                    is_final = True
                new_state = dfa.new_state(all_follow_pos, is_final)
                u += 1
            dfa.add_transition(dfa.get_state(p), ch, new_state)
        p += 1


if __name__ == '__main__':
    sys.exit(main());
