# Authors: Joshua Go, Evan Swanson, Mauricio Velazquez
# Course: CPSC 450
# Assignment: Final Project
# Usage: python3 main.py [test file name]
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
    adj_list = []   # adjacency list containing friends of the users based on the users index
    user_dict = {}    # dictionary containing the users and their corresponding index
    j = 0
    user = None
    users_friend = None
    for i in filename.readline().split(): 
        if j == 0:
            user = i
            user_dict = {i : j}     # add user to the user dictionary      
        elif j == 1:
            users_friend = i
            user_dict = {i : j}     # add user to the user dictionary
        else:
            users_friends_dict = {users_friend : i}  # add the users friend to a dictionary
            adj_list.append(users_friends_dict)     # add that dictionary to the adjacency list
        j += 1
    print(adj_list)
    
# takes in command line arguments to execute program
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file' % sys.argv[0])
    main(sys.argv[1])