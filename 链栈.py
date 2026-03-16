class listnode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkStack:
    def __init__(self):
        self.head = None

    def push(self,item):
        node = listnode(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head:
            raise Exception("pop from empty stack")
        else:
            cur = self.head
            self.head = self.head.next
            cur.next = None
            return cur.val


if __name__ == "__main__":
    ls = LinkStack()
    ls.push(100)
    ls.push(200)
    ls.push(300)
    print(ls.pop())

