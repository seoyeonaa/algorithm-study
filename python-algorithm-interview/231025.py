# 7. 팰린드롬 연결리스트
# leetcode 234
# 연결 리스트가 팰린드롬 구조인지 판별하라
# 1 -> 2 == False, 1 -> 2 -> 2 -> 1 == True


# 나의 풀이
# pop으로 앞 뒤가 다른지 확인하기
lst = [1, 2, 2, 1]


def myPalindrome(lst=list[int]) -> int:
    while len(lst) > 1:
        if lst.pop(0) != lst.pop():
            return False

    return True


myPalindrome(lst)


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node_2 = ListNode(2)
node_1 = ListNode(1, node_2)

node_6 = ListNode(1)
node_5 = ListNode(2, node_6)
node_4 = ListNode(3, node_5)
node_3 = ListNode(2, node_4)
node_2 = ListNode(1, node_3)


# A-1) 연결 리스트를 리스트로 변환하여 풀이
def isPalindrome(head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


# A-2) 데크를 이용한 최적화
# 위의 pop 연산은 첫 값을 꺼내오면 모든 값이 한 칸씩 시프팅되며, 시간 복잡도 O(n)이 발생하기 떄문이다.
import collections


def isPalindrome_mk2(head: ListNode) -> bool:
    # 데크 자료형 선언
    q = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


# A-3) 런너를 이용한 풀이
def isPalindrome_mk3(head: ListNode) -> bool:
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next  # 두 칸씩 이동
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


isPalindrome_mk3(node_2)
