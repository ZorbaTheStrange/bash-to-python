#! /usr/bin/env python3
'''
cat.py - Copy of the Unix 'cat' command.
'''

import sys, argparse, os


def parse_args():
    '''
    unix command cat
    '''

    parser = argparse.ArgumentParser()

    parser.add_argument('file_path',
                        nargs='*',
                        type=str,
                        help='The file to be concatenated, moved to another file')
   
    parser.add_argument('-n',
                        dest='number_line',
                        action='store_true',
                        default=False,
                        help='Number all ouput lines.')

    parser.add_argument('-E',
                        dest='show_ends',
                        action='store_true',
                        default=False,
                        help='display $ at the end of each line.')

    return parser.parse_args()


def cat(file_path, number_line=False, show_ends=False):
    '''
    Unix command cat

    Args:
        fileOne (str|list):         File to concatenate.
        numberLine (bool):          Number all output. lines 
        showEnds (bool):            display $ at end of each line. 
    '''
    
    if not os.path.exists(file_path[0]):
        sys.stdout.write('cat: {0}: No such file or directory.\n'.format(file_path))
        return False
    
    with open(file_path[0], 'r') as f:
        content = f.read()
        f.close()
     
        if show_ends:
            content = content.replace('\n', '$\n')

        if number_line:
            count = 1
            for line in content.split('\n'):
                sys.stdout.write('{0:>5} {1}\n'.format(count, line))
                count += 1                    
        else:
            sys.stdout.write(content)


def main():
    '''
    Main 
    '''

    args = parse_args()
    cat(args.file_path, args.number_line, args.show_ends)


if __name__ == '__main__':
    sys.exit(main())
