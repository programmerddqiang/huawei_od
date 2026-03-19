# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections
import math
from itertools import combinations
from re import match

height = [int(x) for x in input().split(" ")]
n = len(height)

idx1 = [0 for x in range(n)]
for i in range(1, n):
    if (idx1[i - 1] > height[i - 1]):
        idx1[i] = idx1[i - 1]
    else:
        idx1[i] = height[i - 1]

idx2 = [0 for x in range(n)]
i = n - 2
while (i >= 0):
    if (idx2[i + 1] > height[i + 1]):
        idx2[i] = idx2[i + 1]
    else:
        idx2[i] = height[i + 1]
    i -= 1

new_height = [0 for x in range(n)]
h_set = set([])
i = 0
while (True):
    if (i >= n - 1):
        break
    else:
        if (max(0, min(idx1[i], idx2[i]) - height[i]) != 0):
            new_height[i] = max(0, min(idx1[i], idx2[i]) - height[i]) + height[i]
            h_set.add(new_height[i])
    i += 1

count = 0
left = 0
right = 0
for ele in h_set:
    start_index = 0
    while (new_height[start_index] < ele or height[start_index] >= ele):
        start_index += 1

    end_index = n - 1
    while (new_height[end_index] < ele or height[end_index] >= ele):
        end_index -= 1

    tmp = 0
    i = start_index
    while (True):
        if (i >= end_index + 1):
            if (tmp > right):
                count = start_index - 1
                left = end_index + 1
                right = tmp
            elif (tmp == right):
                if (end_index - start_index + 1 < left - count - 1):
                    count = start_index - 1
                    left = end_index + 1
            break
        else:
            if (ele - height[i] > 0):
                tmp += ele - height[i]
        i += 1

if (right == 0):
    print(0)
else:
    print(str(count) + " " + str(left) + ":" + str(right))
