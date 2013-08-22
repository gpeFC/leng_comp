#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
22/08/2013
Emanuel G.P.
Lenguajes y Compiladores.
Facultad de Ciencias, UAEM.
>>Common I/O operations<<
"""

import sys
import os
import pickle

def read_file(name):
    f = open(name, "r")
    # Notice that we can iterative thru the file object.
    for line in f:
        print "->", line, 
    f.close()

if __name__ == "__main__":
    print "Hi there!"
    name = raw_input("What's you name? ")
    print "Hello {}".format(name)
    age = raw_input("How old are you? ")
    age = int(age)
    print "So, you are {1} years old, {0}".format(name, age)
    print "you have lived more than %5.2f months!" % (age*12)
    print "\nI will read me thru a function and spit it line by line"
    read_file(sys.argv[0])
    
    print "I can also print to a file"
    f2 = open("tmp.txt", "w")
    f2.write("1 line\n");
    f2.write("2 line\n");
    f2.write("3 line\n");
    f2.write("4 line\n");
    f2.write("5 line\n");
    f2.close()
