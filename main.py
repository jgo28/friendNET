# Authors: Joshua Go, Evan Swanson, Mauricio Velazquez
# Course: CPSC 450
# Assignment: Final Project
# Usage: python3 main.py [test file name]
# Description:
#   
# ----------------------------------------------------------------------
#  Killer Feature 1: 
#      Recommended friends. We would go through all of a user's friends'
#      friends and count up how many of them are recurring throughout. If 
#      If the friend that popped up the most is not friends with the user, 
#      it will be a recommended friend. 
# ----------------------------------------------------------------------

import sys

def main(filename):
    try:
        file_stream = open(filename, 'r')
        userDictionary, adjacencyList = read_file(file_stream) 
        file_stream.close()
    except FileNotFoundError:
        sys.exit('invalid filename %s' % filename)
    userChoice = 0
    while(userChoice != 3):
        print("What do you want to do?")
        print("1) Check if user exists")
        print("2) Check connection between users")
        print("3) Quit")
        userChoice = input()
        #just test cases, replace with actual params
        doChoice(userChoice, userDictionary, adjacencyList)

# reads file
def read_file(filename):
    adj_list = []   # adjacency list containing friends of the users based on the users index
    user_dict = {}    # dictionary containing the users and their corresponding index
    every_three = 0     # resets counter every 3 iterations
    index = 0   # keeps track of index of the adjacency list
    user = None
    users_friend = None
    for i in filename.read().split(): 
        if every_three == 0:
            user = i
            if not i in user_dict:
                user_dict.update({i : index})     # add user to the user dictionary  
                index += 1  # update index
        elif every_three == 1:
            users_friend = i
        else:
            users_friends_dict = {users_friend : i}  # add the users friend to a dictionary
            adj_list.append(users_friends_dict)     # add that dictionary to the adjacency list
        every_three += 1
        if every_three == 3:    # reset to 0 every 3 iterations
            every_three = 0
    return user_dict, adj_list
    
def doChoice(userChoice, userDictionary, graph):
    if userChoice == 1:
        checkName = raw_input("Enter the users name > ")
        if checkName in userDictionary:
            print(checkName + " exists")
        else:
            print(checkName + " does not exist")
    elif userChoice == 2:
        names = raw_input("What users (seperated by spaces) > ")
        names = names.split()
        if names[1] in graph[userDictionary[names[0]]]:
            weight = graph[userDictionary[names[0]]][names[1]]
            print("The connection from " + names[0] + " to " + names[1] + " has weight " + str(weight))
        else:
            print("No connection between names")


# takes in command line arguments to execute program
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file' % sys.argv[0])
    main(sys.argv[1])