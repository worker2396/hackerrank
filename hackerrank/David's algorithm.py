import collections as cl
import numpy as np

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
# 0 2 1
# 1 1 1
# 2 0 0
# if a list

def compare(s, t):
    return cl.Counter(s) == cl.Counter(t)


def sum_row(container, it, size):
    total = 0
    for i in range(size):
        total += container[it][i]
    return total


def sum_col(container, it, index_start, size):
    total = 0
    for i in range(index_start, index_start + size):
        total += container[i][it]
    return total


def sum_check(container, index_start, size):
    row_list = []
    col_list = []

    for i in range(index_start, index_start + size):
        row_list.append(sum_row(container, i, size))

    for j in range(size):
        col_list.append(sum_col(container, j, index_start, size))

    return compare(row_list, col_list)


def organizingContainers(container):
    # Write your code here
    queries = container[0][0]
    count = 0
    length = len(container)
    size = container[1][0]
    index_start = 2
    head_index = 1
    while count < queries:
        if sum_check(container, index_start, size):
            print('Possible')
        else:
            print('Impossible')
        head_index += size + 1
        count += 1
        if head_index < length:
            size = container[head_index][0]
            index_start = head_index + 1


# sample inputs
two_d_array = [[2],  # 0
               [3],  # 1
               [1, 3, 1],  # 2
               [2, 1, 2],  # 3
               [3, 3, 3],  # 4
               [3],  # 5
               [0, 2, 1],  # 6
               [1, 1, 1],  # 7
               [2, 0, 0]]  # 8

two_d_array_2 = [[2],
                 [3],
                 [1, 3, 1],
                 [2, 1, 2],
                 [3, 3, 3],
                 [4],
                 [2, 4, 1, 0],
                 [0, 2, 3, 0],
                 [0, 3, 2, 0],
                 [0, 0, 0, 2]]

big_2d_array = np.ones((1002, 1000), int)
big_2d_array[0] = [1]
big_2d_array[1] = [1000]

organizingContainers(two_d_array)
organizingContainers(two_d_array_2)
organizingContainers(big_2d_array)
