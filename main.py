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
    userChoice = 0
    while(userChoice != 3):
        print("What do you want to do?")
        print("1) Check if user exists")
        print("2) Check connection between users")
        print("3) Quit")
        userChoice = input()
        #just test cases, replace with actual params
        doChoice(userChoice, {'a': 0, 'b' : 1}, [{'b':10},{'a':5}])

# reads file
def read_file(filename):
    print("read file")

def doChoice(userChoice, userDictionary, graph):
    if userChoice == 1:
        checkName = raw_input("Enter the users name > ")
        print(checkName)
        if checkName in userDictionary:
            print(checkName + " exists")
        else:
            print(checkName + " does not exist")
    elif userChoice == 2:
        names = raw_input("What users (seperated by spaces) > ")
        names = names.split()
        if names[0] in userDictionary and names[1] in userDictionary:
            weight = graph[userDictionary[names[0]]][names[1]]
            print("The connection from " + names[0] + " to " + names[1] + " has weight " + str(weight))
        else:
            print("Invalid input names")


# takes in command line arguments to execute program
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s file' % sys.argv[0])
    main(sys.argv[1])