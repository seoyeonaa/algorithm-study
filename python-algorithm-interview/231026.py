# 7. 두 정렬의 리스트의 병합
# leetcode 21
# 재귀 구조로 연결
# 1-> 2-> 4, 1-> 3-> 4


from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1
