"""
链表构造节点类
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList:
    def __init__(self):
        """
        初始化一个空列表
        """
        self.head = None

    def is_empty(self):
        return self.head == None

    def append(self, item):
        node = ListNode(item)
        if not self.head:
            self.head = node

        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.next = None

    def travel(self):
        if not self.head:
            print("空")
        else:
            cur = self.head
            while cur:
                print(cur.val, end=" ")
                cur = cur.next
            print()

    def remove(self, item):
        """
        移除链表中的一个节点
        :param item:数据区
        :return:None 节点不存在则抛出异常
        """
        # 空列表
        if not self.head:
            raise Exception("x not in LinkList")
        # 删除头结点情况
        if self.head.val == item:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next:
            if cur.next.val != item:
                cur = cur.next
            else:
                cur.next = cur.next.next
                return
        raise Exception("x not in LinkList")

    def len(self):
        """
        获取链表长度
        :return: length
        """
        count = 1
        pre = self.head
        while pre:
            count += 1
            pre = pre.next
        return count

    def insert(self, index, item):
        """
        在指定索引位置插入一个节点
        :param index:索引值
        :param item:数据区
        :return: none | 抛出异常
        """
        if index < 0:
            raise Exception("index error")
        node = ListNode(item)
        cur = self.head
        # 在头结点插入
        if index == 0:
            node.next = cur.next
            self.head = node
            return
        if index > self.len() - 1:
            self.append(item)
            return
        for i in range(index - 1):
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def pop(self):
        """
        在链表尾部弹出一个节点
        :return:尾节点的数据
        """
        length = self.len()
        if length == 0:
            raise Exception("pop from empty linklist")
        cur = self.head
        if length == 1:
            item = self.head.val
            self.head = None
            return item
        while cur.next.next:
            cur = cur.next

        item = cur.next.val
        cur.next = cur.next.next
        return item


if __name__ == "__main__":
    ls = LinkList()
    print(ls.is_empty())
    ls.append(12)
    ls.append(13)
    ls.append(14)
    ls.travel()


