class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def print_tree(self,root):
        if not root:
            return

        list1 = [root]
        list2 = []
        while list1:
            cur_node = list1.pop(0)
            print(cur_node.val,end=" ")
            if cur_node.left:
                list2.append(cur_node.left)
            if cur_node.right:
                list2.append(cur_node.right)

            # 交换变量
            if not list1:
                list1, list2 = list2, list1
                print()

class Solution2:
    def print_tree(self,root):
        if not root:
            return
        list1 = [root]
        list2 = []
        level = 1
        while root:
            cur_node = list1.pop()
            print(cur_node.val,end=" ")
            if level%2:
                if cur_node.left:
                    list2.append(cur_node.left)
                if cur_node.right:
                    list2.append(cur_node.right)
            else:
                if cur_node.right:
                    list2.append(cur_node.right)
                if cur_node.left:
                    list2.append(cur_node.left)

            if not list1:
                list1, list2 = list2, list1
                print()
                level += 1


if __name__ == '__main__':
        pass