#! /usr/bin/env python
'''
head.py - Unix copy of head command. 
'''


import sys, argparse, os

def parse_args():
    '''
    command line arguments
    '''

    parser = argparse.ArgumentParser()

    parser.add_argument('file_path',
                        nargs='*',
                        type=str,
                        help='file path to print first ten lines.')

    parser.add_argument('-v',
                        dest='verbose',
                        action='store_true',
                        default=False,
                        help='always output headers giving file names')

    parser.add_argument('-n',
                        dest='lines_out_put',
                        nargs='?',
                        default=10,
                        type=int,
                        help='Number of lines to output instead of 10.')

    return parser.parse_args()


def head(file_path, verbose=False, lines_out_put=10):
    '''
    Unix command head

    Args:
        file_path (str|list):          File for printing out first 10 lines.
        verbose (bool):                Always output headers giving file name.
    '''

    if verbose:
        sys.stdout.write(str('==>' + file_path[0] +'<==' + '\n'))

    with open(file_path[0], 'r') as f:
        lines = [next(f) for x in xrange(lines_out_put)]
        sys.stdout.write('\n'.join(lines))


def main():
    '''
    main
    '''

    args = parse_args()
    head(args.file_path, args.verbose, args.lines_out_put)


if __name__ =='__main__':
    sys.exit(main())
