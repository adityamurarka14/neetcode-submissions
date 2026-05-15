# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        myStack = [(p,q)]

        while myStack:
            node1, node2 = myStack.pop()

            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            myStack.append((node1.left, node2.left))
            myStack.append((node1.right, node2.right))

        
        return True

        # if not p and not q:
        #     return True
        # if not p or not q or p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)