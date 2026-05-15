# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kthNode = self.getK(groupPrev, k)
            if not kthNode:
                break
            
            groupNext = kthNode.next

            prev, curr = kthNode.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tempPrev = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tempPrev
        
        return dummy.next
    
    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        

    # def reverseLL(self, head):
    #     prev = None
    #     curr = head

    #     while curr:
    #         temp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp
        
    #     return prev