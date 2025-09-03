##################################################################################
# Module - library that has one or more feature built into it. reusability of code
#        - internal package. implemented in a folder
# random - function included in python. example of a module.
# import - allows you to import modules in python
# from - can use when importing in a specific module
########################################################
#import random

############################
# from random import choice
#############################
# seq - a list or list like
##############################
# coin = random.choice(seq=["heads", "tails"])
# print(coin)

##################################
# randint(a, b) - get a random int
##################################

# number = random.randint(1, 10)
# print(number)

#################################################################
# shuffle(x) - list of values then shuffles them in random order
#################################################################

# cards = ["jack", "queen", "king"]
# random.shuffle(cards)
#
# for card in cards:
#     print(card)

########################################################################################
# statistics - library contains all sort of functions doing. calculating means, median
# average - function allows you to average the numbers you pass in
########################################################################################

# import statistics
#
# print(statistics.mean([100, 90]))
##########################################################################################
# command-line arguments - allow you to provide input not when prompted inside of a program as happens when we call function input
#                        - allows you to provide arguments that is input into the program just when you are executing on the command line
#                        - provide words or number after you are typing and passed to the program itself
##########################################################################################

#####################################################################################################
# sys.argv - argument vector. the list of all the words that type in the prompt before hitting enter
#####################################################################################################

#import sys

# try:
#     print("hello, my name is", sys.argv[1])
# # except IndexError:
# #     print("Too few arguments")

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])

#################
# Another option

# Check for errors
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
#
# # Print name tags
# print("Hello, my name is", sys.argv[1])


##################################################
# Another option
# sys.exit - exit the program per line prematurely

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
#
# # Print name tags
# print("Hello, my name is", sys.argv[1])

##################################################
# Another option
# slices - to take a subset of data structure like a list or a slice of a list

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
#
# for arg in sys.argv[1:]:
#     print("Hello, my name is", arg)

#####################################################################################################
# packages - 3rd party libraries outside python.
# PyPI - Python Package Index. Website is pypi.org to download packages
# cowsay - package in python. pypi.org/project/cowsay
# pip - package manager available in python. allows you to install your package by running a command
# ascii art - to print picture in the screen

# import cowsay
# import sys
#
# if len(sys.argv) == 2:
#  #   cowsay.cow("hello, " + sys.argv[1])
#      cowsay.trex("hello, " + sys.argv[1])

##################################################################################################
# APIs - Application Programming Interface - 3rd party services that a code talk to
#      - pretends to be a browser and connects with a 3rd party API then incorporate to the program
# request - a library that allows you to make web or internet request using python code for the retrieval of URLs http or https
# https://itunes.apple.com/search?entity=song&limit=1&term=weezer
# JSON - JavaScript Object Notation
#      - used as language agnostic format for exchanging data between computers
#      - no need to install, already included in python
# import json
# import requests
# import sys
#
# if len(sys.argv) != 2:
#     sys.exit()

################################################################################
# request.get - function inside request package that get response from a server
###############################################################################
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#######################################################
# json.dumps - function inside json. json dump string
#######################################################

# print(json.dumps(response.json(), indent=2))

# o = response.json()
# for result in o["results"]:
#     print(result["trackName"])

#########################
# make your own library

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

#########################################################################################################
# __name__ - variable special symbol who's value is automatically set by python to be "main" when you run a file on from the command line

if __name__ == "__main__":
    main()
