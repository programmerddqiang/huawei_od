"""
竖直四子棋
"""


# 代码可以处理4行一下的矩阵

def check(matrix, x, y):
    """
    检查是否有四子连线
    :param matrix: 棋盘矩阵
    :param x: 当前棋子的行号
    :param y: 当前棋子的列号
    :return: 是否有四子连线
    """
    h = len(matrix)  # 矩阵行数
    l = len(matrix[0])  # 矩阵列数
    count = 0  # 统计相同的棋子
    jishu = 3  # 四个棋子只要统计三次

    # 检查纵向四棋子
    if x < h - 3:  # 保证下面至少有三个
        a = x
        while jishu != 0 and matrix[a][y] == matrix[a + 1][y]:
            count += 1
            jishu -= 1
            a += 1
        if count == 3:
            return True
        count = 0
        jishu = 3

    # 检查左边横向四棋子
    if y >= 3:
        b = y
        while jishu != 0 and matrix[x][b] == matrix[x][b - 1]:
            count += 1
            jishu -= 1
            b -= 1
        if count == 3:
            return True
        count = 0
        jishu = 3

    # 检查右边横向四棋子
    if y < l - 3:
        b = y
        while jishu != 0 and matrix[x][b] == matrix[x][b + 1]:
            count += 1
            jishu -= 1
            b += 1
        if count == 3:
            return True
        count = 0
        jishu = 3

    # 检查左边斜向四棋子
    if x < h - 3 and y >= 3:
        a, b = x, y
        while jishu != 0 and matrix[a][b] == matrix[a + 1][b - 1]:
            count += 1
            jishu -= 1
            a += 1
            b -= 1
        if count == 3:
            return True
        count = 0
        jishu = 3

    # 检查右边斜向四棋子
    if x < h - 3 and y < l - 3:
        a, b = x, y
        while jishu != 0 and matrix[a][b] == matrix[a + 1][b + 1]:
            count += 1
            jishu -= 1
            a += 1
            b += 1
        return count == 3

    return False


########################################################################
# 读取输入
m, n = map(int, input().split())  # 行数和列数
nums = list(map(int, input().split()))

# 初始化棋盘
matrix = [[0] * m for _ in range(n)]
isOver = False

# 处理每一步棋
for i in range(len(nums)):
    index = -1
    color = 1 if i % 2 == 0 else 2  # 偶数下标为red用1表示，奇数下标为blue用2表示
    num = nums[i]

    # 检查输入是否合法
    if num <= 0 or num > m or matrix[0][num - 1] != 0:  # 输入的数不能小于等于0或者不能大于列数或者所在的列不能满
        print(f"{i + 1},error")
        isOver = True
        break

    # 找到可以放置棋子的位置
    for j in range(n - 1, -1, -1):  # 从下往上找
        if matrix[j][num - 1] == 0:  # 第j行第num-1列等于0
            index = j
            matrix[j][num - 1] = color
            break

    if index == -1:  # 没找到退出
        print(f"{i + 1},error")
        isOver = True
        break
    # index为行号
    # 第七个棋子开始才能形成四子连线
    if i >= 6 and check(matrix, index, num - 1):
        print(f"{i + 1},{'red' if color == 1 else 'blue'}")
        isOver = True
        break

if not isOver:
    print("0,draw")  # 无胜负
