import math
import os
import random
import re
import sys

# def repeatedString(s, n):
#     i = 0
#     j = 0
#     count = 0
#     str_list = []
#     str_list[:0] = s
#     while i < n:
#         j = i % len(str_list)
#         if str_list[j] == 'a':
#             count += 1
#         i += 1
#     return count

s = 'aba'
n = 10

def repeatedString(s, n):
    i = 0
    j = 0
    freaquency = 0
    count = 0
    str_list = []
    str_list[:0] = s
    size = len(str_list)
    for it in range(size):
        if str_list[it] == 'a':
            freaquency += 1
    if size > 1:
        times = n//size
        index = n%size
        count = times*freaquency
        for j in range(index):
            if str_list[j] == 'a':
                count+=1
    else:
        if str_list[0] == 'a':
            count = n
    return count

print(repeatedString(s,n))


    # Write your code here



