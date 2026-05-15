# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head:
        #     return None
        # nodeLen = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     nodeLen += 1
        # removeIndex = nodeLen - n
        # if removeIndex == 0:
        #     return head.next
        # curr = head
        # for i in range(nodeLen - 1):
        #     if (i+1) == removeIndex:
        #         curr.next = curr.next.next
        #         break
        #     curr = curr.next
        # return head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n>0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
