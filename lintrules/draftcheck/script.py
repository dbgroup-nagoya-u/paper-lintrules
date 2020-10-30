#####################################################################
# This file was forked from https://github.com/ebnn/draftcheck.
# That project would be MIT LICENSE since some URL show its LICENSE.
# See https://libraries.io/pypi/draftcheck
# See also https://pypi.org/project/draftcheck/
#####################################################################

from .rules import get_brief
from .validator import Validator


def pad_string(text, span, size):
    left_str = text[max(0, span[0] - size):span[0]]
    right_str = text[span[1]:min(len(text), span[1] + size)]

    text_format = '{0}{1}{2}'

    if len(left_str) == size:
        text_format = '...' + text_format

    if len(right_str) == size:
        text_format += '...'

    padded_str = text_format.format(left_str, text[span[0]:span[1]], right_str)
    start_index = len(left_str) + (3 if len(left_str) == size else 0)

    return padded_str, start_index


def print_warning(fname, lineno, line, span, rule, args):
    prefix = f'{fname}:{lineno}:{span[0]}:'
    print(prefix, end=' ')
    print(f"\t[{rule.id:03d}]", get_brief(rule))


def remove_latex_comment(line):
    for i in range(len(line)):
        if line[i] == '%':
            if i > 0 and line[i - 1] == "\\":
                if i > 1 and line[i - 2] == "\\":
                    return line[:i + 1]
                continue
            return line[:i + 1]
    return line

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Check for common mistakes in LaTeX documents.')

    parser.add_argument('filenames', action='append',
                        help='List of filenames to check')

    args = parser.parse_args()

    # Count the total number of errors
    num_errors = 0

    # XXX: This code is verbose, but it'd be good for reviewdog paser.
    for fname in args.filenames:
        with open(fname, 'r') as infile:
            validator = Validator()
            for lineno, line in enumerate(infile):
                line = remove_latex_comment(line)
                for rule, span in validator.validate(line):
                    num_errors += 1

    if num_errors > 0:
        print(f'\nTotal of {num_errors} mistakes found.')
    else:
        print('No mistakes found.')

    for fname in args.filenames:
        with open(fname, 'r') as infile:
            validator = Validator()
            for lineno, line in enumerate(infile):
                line = remove_latex_comment(line)
                for rule, span in validator.validate(line):
                    print_warning(fname, lineno + 1 , line.strip(), span, rule, args)

    if num_errors > 0:
        return 1
    else:
        return 0
