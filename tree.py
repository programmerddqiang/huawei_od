class TreeNode:
    def __init__(self, val):
        """
        结点类：创建结点
        :param val:
        """
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """
        初始化一个空树：根节点为None
        """
        self.root = None

    def add(self, item):
        """
        二叉树中添加一个节点
        :param item: 数据区
        :return: None
        """
        node = TreeNode(item)
        if not self.root:
            self.root = node
            return
        # 队列的思想
        node_queue = [self.root]
        while True:
            cur_node = node_queue.pop(0)
            if cur_node.left:
                node_queue.append(cur_node.left)
            else:
                cur_node.left = node
                break
            if cur_node.right:
                node_queue.append(cur_node.right)
            else:
                cur_node.right = node
                break

    def bfs(self):
        if not self.root:
            return None

        node_queue = [self.root]
        while node_queue:
            cur_node = node_queue.pop(0)
            print(cur_node.val, end=" ")

            if cur_node.left:
                node_queue.append(cur_node.left)

            if cur_node.right:
                node_queue.append(cur_node.right)

        print()


    def dfs(self):



if __name__ == "__main__":
    bt = BinaryTree()
