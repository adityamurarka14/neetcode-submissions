# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowptr = head
        fastptr = head
        if head == None:
            return False
        while fastptr.next and fastptr.next.next != None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if fastptr == slowptr:
                return True

        return False

