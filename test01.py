"""

"""
import collections

li = collections.deque([1, 2, 3])  # 普通列表删除效率低
print(li)
li.popleft()
print(li)

#####################
# 手动设置递归深度
import sys

sys.setrecursionlimit(1000000)
