# regex-to-dfa
University homework for creating a DFA from a REGEX

This tool receives as input:
  - the alphabet of the expression
  - the regular expression written in infix notation

Supported operators are: union, concatenation and Kleene iteration(*)

## How the DFA is constructed

## Usage

```bash
usage: regex-to-dfa.py [-h] [--visualizer]
                       alphabet, regex
arguments:
  alphabet           The alphabet of the regular expression
  regex              Actual regex, between single quotes

optional argument:
  --visualizer       Makes dfa.out file with the DFA in a specific format.
```

To actually visualize the DFA you need to:
  - run the [graphivz_web](https://github.com/hythof/graphviz_web) tool
  - copy paste the content of the `dfa.out` file in the online tool

## Example
```bash
regex-to-dfa.py abcdefghijklmnopqrstuvwxyz '((a|bb)*(ba|c)*ca)*'
```
