#! /usr/bin/env python

'''
tail.py - Copy of the Unix tail command.
'''

import sys, argparse, os


def parse_args():
    '''
    command line arguments.
    '''

    parser = argparse.ArgumentParser()

    parser.add_argument('file_path',
                        nargs='*',
                        type=str,
                        help='file path to print last ten lines.')

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

def tail(file_path, verbose=False, lines_out_put=10):
    '''
    Unix command cat

    Args: 
        file_path (str|list):             File for printing out last 10 lines.
        verbose (bool):                 Always output headers giving file name.
        lines_out_put: (int)            Number of lines to output instead of 10
    ''' 
    
    block_size = 1024
    ten_lines = []
    block_num = -1
    lines_out = lines_out_put
        
 
    with open(file_path[0], 'r') as f:
        f.seek(0, 2)
        end_byte = f.tell()
        
        if verbose:
            sys.stdout.write('==>' + str(file_path[0]) + '<==')


        while lines_out > 0 and end_byte > 0:
            if (end_byte - block_size > 0):
                f.seek(block_size * block_num, 2)
                ten_lines.append(f.read(block_size))

            else:
                f.seek(0, 0)
                ten_lines.append(f.read(end_byte))

            lines_found = ten_lines[-1].count('/n')
            lines_out_put -= lines_found
            end_byte -= block_size
            block_num -= 1

        read_text = ''.join(reversed(ten_lines))

        sys.stdout.write('\n'.join(str(read_text).splitlines()[-lines_out:])) 
             

def main():
    '''
    main
    '''
 
    args = parse_args()
    tail(args.file_path, args.verbose, args.lines_out_put)


if __name__ == '__main__':
    sys.exit(main())
