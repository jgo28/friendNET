# Authors: Joshua Go, Evan Swanson
# Course: CPSC 450
# Assignment: Final Project
# Description:
#   
# ----------------------------------------------------------------------

import sys

def main(filename):
    try:
        file_stream = open(filename, 'r')
        read_file(file_stream)
        file_stream.close()
    except FileNotFoundError:
        sys.exit('invalid filename %s' % filename)

# reads file
def read_file(filename):
    print("read file")

# takes in command line arguments to execute program
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file' % sys.argv[0])
    main(sys.argv[1])