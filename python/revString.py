#!/usr/bin/env python3.7

# Reverse string 
# references: 
#     https://appdividend.com/2019/05/24/how-to-reverse-string-in-python-python-reverse-string-example/

import sys

str_to_reverse = input ("Input the string you want to reverse: ")
reversed_str = str_to_reverse[::-1]

print ("The reversed string is: ", reversed_str)
