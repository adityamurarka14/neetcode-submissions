# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
    #     if not l1 and not l2 and carry == 0:
    #         return None

    #     v1 = l1.val if l1 else 0
    #     v2 = l2.val if l2 else 0

    #     carry, val = divmod(v1 + v2 + carry, 10)

    #     next_node = self.add(
    #         l1.next if l1 else None,
    #         l2.next if l2 else None,
    #         carry
    #     )
    #     return ListNode(val, next_node)
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # return self.add(l1, l2, 0)

        dummy = ListNode()
        overFlow = 0
        prev = dummy
        while l1 or l2 or overFlow:
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

        return dummy.next