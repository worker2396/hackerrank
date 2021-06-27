import math
import os
import random
import re
import sys


steps = 8
path = 'UDDDUDUU'



def countingValleys(steps, path):
    valleys = 0
    height = 0
    for move in path:
        if move == 'U':
            height += 1
            if height == 0:
                valleys += 1
        elif move == 'D':
            height -= 1

    return valleys