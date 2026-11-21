# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = head
        n = 0
        while end.next:
            end = end.next
            n += 1
        
        def moveNode(head:Optional[ListNode], n: int) -> None:
            for n in range(n):
                head = head.next
            return head

        curr = head
        for i in range(n//2):
            temp = curr.next
            prev = moveNode(curr, n - 2*i - 1)
            end = prev.next
            prev.next = None
            curr.next = end
            end.next = temp
            curr = temp