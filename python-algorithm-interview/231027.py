# 8. 역순 연결 리스트
# leetcode 206
# 연결 리스트를 뒤집어라
# 1->2->3->4->5->NULL
# 5->4->3->2-?1->NULL

# 재귀? 반복?

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node_5 = ListNode(5)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)


def reverseList(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode):
        if not node:
            return prev
        next, node.next = node.next, prev  # next -> 다음 노드, node.next -> 이전 노드?
        # 1-prev
        # 2-1-prev
        # 3-2-1-prev
        # 4-3-2-1-prev
        return reverse(next, node)

    return reverse(head)
