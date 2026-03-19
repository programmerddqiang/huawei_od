"""
蓄水池
"""
# coding:utf-8
# JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。
import functools
import collections
import math
from itertools import combinations
from re import match

params = [int(x) for x in input().split(" ")]

def trap(height):
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    ans = 0
    left_bound = n      # 最左边积水柱子的索引
    right_bound = -1    # 最右边积水柱子的索引
    while left < right:
        water_level = min(left_max, right_max)
        # 处理左边
        if height[left] <= water_level:
            if water_level - height[left] > 0:  # 真正有积水
                ans += water_level - height[left]
                left_bound = min(left_bound, left)
                right_bound = max(right_bound, left)
            left += 1
            continue
        # 处理右边
        if height[right] <= water_level:
            if water_level - height[right] > 0:
                ans += water_level - height[right]
                left_bound = min(left_bound, right)
                right_bound = max(right_bound, right)
            right -= 1
            continue
        # 更新左右最大值
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
    # 输出结果
    if left_bound > right_bound:
        print(0)
    else:
        print(left_bound-1, right_bound+1)
        print(ans)
    return ans

trap(params)

