# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3 4 None
        # none 1 2 3 4
        prev = None
        curr = head

        while curr:
            nxt = curr.next  # address of 2 in next
            curr.next = prev  # assigning 1 next address none
            prev = curr  # prev jumps to 1
            curr = nxt  # curr jumps to 2

        return prev


# Pattern: Iterative Three-Pointer Reversal (prev, curr, nxt in-place pointer rewiring)
# Time: O(n) | Space: O(1)
