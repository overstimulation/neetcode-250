import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: "ListNode | None"
    ) -> "ListNode | None":
        if not head or not head.next:
            return head

        curr = head
        while curr and curr.next:
            gcd_val = math.gcd(curr.val, curr.next.val)
            new_node = ListNode(gcd_val, curr.next)
            curr.next = new_node
            curr = new_node.next

        return head
