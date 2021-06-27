import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    # Write your code here
    socks = {}
    pairs = 0
    for i in range(n):
        if ar[i] not in socks:
            socks[ar[i]] = 1
        else:
            socks[ar[i]] = socks[ar[i]] + 1
    # print(socks)
    for value in socks.values():
        pairs += value // 2
    return pairs


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
ar2 = [10, 20, 20, 10, 10, 30, 50, 10, 20, 50]

print(sockMerchant(9, ar))
print(sockMerchant(10, ar2))
