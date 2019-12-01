#!/usr/bin/env python3.7

# generate random integer values
# use secrets instead of random, for security reasons

from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers

for i in range(10):
    rNumber = randint(0, 10)
    print(rNumber)


