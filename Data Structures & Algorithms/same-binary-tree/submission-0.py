# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackp = [p]
        stackq = [q]

        while stackp and stackq:
            nodep = stackp.pop()
            nodeq = stackq.pop()

            # If both are None, continue
            if not nodep and not nodeq:
                continue
            # If one is None or values don't match
            if not nodep or not nodeq or nodep.val != nodeq.val:
                return False

            # Push children in same order
            stackp.append(nodep.right)
            stackp.append(nodep.left)
            stackq.append(nodeq.right)
            stackq.append(nodeq.left)

        # If one stack is not empty
        return not stackp and not stackq