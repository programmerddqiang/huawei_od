class LinkList:
    def __init__(self):
        self.head = None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reversed_link_list(self, head):
        cur = head
        pre = None
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        head = pre
        return head


if __name__ == "__main__":
    head = ListNode(100)
    head.next = ListNode(200)
    head.next.next = ListNode(300)
    s = Solution()
    pre = s.reversed_link_list(head)
    while pre:
        print(pre.val)
        pre = pre.next
