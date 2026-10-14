# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Special case: single-node list
        if head.next is None:
            return None

        # First, count the length
        N = 1
        length = head
        while length.next is not None:
            length = length.next
            N += 1

        removeIndex = N - n

        # Special case: removing the head
        if removeIndex == 0:
            return head.next

        # Traverse to the node just before the one to remove
        i = 0
        prev = None
        curr = head
        while i < removeIndex:
            prev = curr
            curr = curr.next
            i += 1

        # Remove the node
        prev.next = curr.next
        curr.next = None

        return head





        