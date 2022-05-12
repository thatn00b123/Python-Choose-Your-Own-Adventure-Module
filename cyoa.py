#!/usr/bin/env python
"""
Python 3.x Choose Your Own Adventure (CYOA) Module.
A module for creating choose-your-own-adventure style games.
"""
# Copyright 2018 by Jacob M
# All rights reserved.
# This file is released under the "MIT License Agreement".
# Please see the LICENSE file that should have been included as part of this package.
__author__ = "Jacob M"
__copyright__ = "Copyright 2022, GPL-3.0 license"
__credits__ = ["Jacob M"]
__license__ = "GPL-3.0"
__version__ = "1.0.2"
__maintainer__ = "Jacob M"
__email__ = "pythonCYOA@outlook.com"
__status__ = "Development"


class ChoiceError(Exception):
    def __init__(self, obj, message="is not a valid choice, text or ending object!"):
        self.obj = obj
        self.message = f"{obj} "
        super().__init__(message)


# CYOA variables
variables = {}  # dictionary for storing variables and their values
endings = []  # list for storing possible endings
gotendings = []  # list for storing endings the player has achived
start = None  # starter choice, text or ending (why though?) SET THIS BEFORE STARTER FUNCTION OR GAME WILL BREAK!

# CYOA functions

# Create a variable named {varname} and set it to {defaultval}
def makevar(varname: str, defaultval=0, raiseerror=False):
    if varname in variables:
        raise KeyError(f"ERROR: VARIABLE {varname} ALREADY EXISTS")
    else:
        variables[varname] = defaultval


# Set variable's value in variables dict object
def setvar(varname: str, value, raiseerror=False):
    try:
        variables[varname] = value
    except:
        if raiseerror:
            raise KeyError(f"ERROR: VARIABLE {varname} DOES NOT EXIST")


# Get variable value from variables dict object
def getvar(varname, raiseerror=False):
    try:
        return variables.get(varname)
    except:
        if raiseerror:
            raise KeyError(f"ERROR: VARIABLE {varname} DOES NOT EXIST")


def starter():
    try:
        start.run()
    except:
        raise ChoiceError(obj)


# simple function to return the "th" of a number (ex 1 = st, 2 = nd, 3 = rd, n>3 = th):
getth = lambda n: "st" if n == 1 else "nd" if n == 2 else "rd" if n == 3 else "th"


class Test:
    def __init__(self):
        self.a = 69  # haha funny number go brrrrrrr


class Choice:
    """
    Class for handling choices
    ARGS:
    name: string value that appears in its parent choice (ex: "open door")
    txt: string value that appears when you choose this choice (ex: "you opened the door to find...")
    onchoose: callable function that runs when the choice is chosen (SET AS 'None' IF NO FUNCTION WILL BE CALLED)
    children: list of child choices
    """

    def __init__(self, name: str, txt: str, onchoose: callable, children: list):
        self.name = name
        self.txt = txt
        self.funct = onchoose
        self.children = children
        self.parent = None
        for i in children:
            i.parent = self

    def run(self):
        print(self.txt)
        for i in range(len(self.children)):
            print(f"({i}) {self.children[i].name}")
        __valid1 = False
        __valid2 = False
        while not __valid1:
            while not __valid2:
                __inp = input()
                try:
                    __inp = int(__inp)
                    __valid2 = True
                except:
                    print("INPUT MUST BE A WHOLE NUMBER")
            try:
                self.children[__inp].run()
                __valid1 = True
            except:
                print(f"NO {__inp}{getth(__inp)} CHOICE")


class Text:
    """
    Class for handling text buffers
    ARGS:
    name: string value that appears in its parent choice (ex: walk inside)
    txt: string value that appers when this is chosen (ex: you walked inside and...)
    nxtobj: object that is ran after the text buffer
    """

    def __init__(self, name, txt, nxtobj):
        self.txt = txt
        self.nxt = nxtobj

    def run(self):
        print(self.txt)
        try:
            self.nxt.run()
        except:
            raise ChoiceError(self.nxt)


class Ending:
    """
    Class for handling endings
    ARGS:
    name: string value that appears in its parent choice (ex: walk inside)
    endname: string value that is stored in endings list (ex: Good ["The" and "Ending" are automatically appended {The {endname} Ending}])
    txt: string value that appers when this is chosen (ex: you walked inside and...)
    sayend: boolean value that deducts if the name will have "[ENDING]" at the begining
    """

    def __init__(self, name: str, endname: str, txt: str, sayend=False):
        self.name = name
        self.sayend = sayend
        if self.sayend:
            self.name = f"[ENDING] {self.name}"
        self.endname = endname
        self.txt = txt

        endings.append(self.endname)

    def run(self):
        print(self.txt)
        print(f"You have achived the {self.endname} ending")
        print("Would you like to play again? (y/n)")
        __inp = input().lower()
        if __inp == "y":
            print("restarting...")
            starter()
        elif __inp == "n":
            print("goodbye!")
            exit()
        else:
            print("EXITING...")
            exit()
