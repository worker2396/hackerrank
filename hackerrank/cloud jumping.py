import math
import os
import random
import re
import sys

n = 7
c = [0, 0, 1, 0, 0, 1, 0]

def jumpingOnClouds(n, c):
    position = 0
    steps = 0
    while position < n - 1:
        if position != n - 2:
            if c[position + 2] == 1:
                position += 1
                steps += 1
            else:
                position += 2
                steps += 1
        else:
            position += 1
            steps += 1
            return steps
    return steps

print(jumpingOnClouds(n,c))