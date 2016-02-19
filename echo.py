#! /usr/bin/env python3

'''
echo.py - Copy of the Unix utility 'echo.' 
'''

import sys
import argparse

def parse_args():
    '''
    command line Argument 
    '''

    parser = argparse.ArgumentParser()

    parser.add_argument('text',
                         nargs='*',
                         type =str,
                         help='Echos give text.')

    parser.add_argument('-n',
                        dest='noNewline',
                        action='store_true',
                        default=False,
                        help='Does not output the trailing newline.')

    parser.add_argument('-e',
                        dest='enableEscapeChars',
                        action='store_true',
                        default=False,
                        help='enable interpretation of backslash escapes')

    return parser.parse_args()


def echo(text, noNewline=False, enableEscapeChars=False):
    '''
    Unix echo command line replica.

    Args:
        test (str|list):            Text to print to screen
        noNewline (bool):             Do not print new line at the end
        enableEscapeChars (bool):   If true, do not escape backslashes.
    '''

    if not isinstance(text, list):
        text = [text]

    output = ''
    for words in text:
    
        if not isinstance(words, str):
            words = str(words)

        if not output:
            output += words

        else:
            output = ' ' + words

    if not noNewline:
        output += '\n'

    if enableEscapeChars:
        output = bytes(words, 'utf-8').decode('unicode_escape')

    sys.stdout.write(output)


def main():
    '''
    main
    '''
    
    args = parse_args()
    echo(args.text, args.noNewline, args.enableEscapeChars)


if __name__ == '__main__':
    sys.exit(main())
