class listnode:
    def __init__(self,val):
        self.next = None
        self.val = val


class Solution:
    def merge_link_list(self,head1, head2):
        """
        合并链表
        :param head1: 第一个链表头结点
        :param head2:
        :return:合并后链表的头结点
        """

        new_head = listnode(-1)
        new_cur = new_head
        cur1 = head1
        cur2 = head2
        while cur1 and cur2:
                if cur1.val <= cur2.val:
                    new_cur.next = cur1
                    cur1 = cur1.next
                else:
                    new_cur.next = cur2
                    cur2 = cur2.next
                new_cur = new_cur.next

                if cur1:
                    new_cur.next = cur1
                else:
                    new_cur.next = cur2


        return new_head.next