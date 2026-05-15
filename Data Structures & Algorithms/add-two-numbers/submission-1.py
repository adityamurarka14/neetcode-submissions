# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        overFlow = 0
        prev = dummy
        while l1 or l2:
            firstNum = l1.val if l1 else 0
            secondNum = l2.val if l2 else 0
            currentSum = firstNum + secondNum + overFlow
            overFlow = currentSum // 10
            remainder = currentSum % 10
            newNode = ListNode(remainder)
            print(currentSum, remainder, overFlow)
            prev.next = newNode
            
            prev = prev.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if overFlow != 0:
            newNode = ListNode(overFlow)
            prev.next = newNode

        return dummy.next