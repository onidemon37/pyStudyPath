#!/bin/env python3.7

print("what is the name: ")
name = input()

#name = "Kevin"
if len(name) >= 6:
    print("name is long")
elif len(name) == 5:
    print("name is 5 chars long")
elif len(name) >= 4:
    print("name is 4 or more chars long")
else:
    print("name is short")
