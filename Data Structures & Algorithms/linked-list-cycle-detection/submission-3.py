# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slowptr = head
        # fastptr = head
        # if head == None:
        #     return False
        # while fastptr and fastptr.next:
        #     slowptr = slowptr.next
        #     fastptr = fastptr.next.next
        #     if fastptr == slowptr:
        #         return True
        # return False
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        
        return False

