# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        nx = curr.next
        curr.next = None

        while nx:
            temp = nx
            nx = temp.next
            temp.next = curr
            curr = temp

        return curr        