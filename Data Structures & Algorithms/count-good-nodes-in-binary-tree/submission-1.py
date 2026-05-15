# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # def dfs(node, maxVal):
        #     if not node:
        #         return 0
            
        #     res = 1 if node.val >= maxVal else 0
        #     maxVal = max(maxVal, node.val)
        #     res += dfs(node.left, maxVal)
        #     res += dfs(node.right, maxVal)
        #     return res
        
        # return dfs(root, root.val)
        if not root:
            return 0
        
        res = 0
        myq = deque([(root, -float('inf'))])

        while myq:
            node, maxVal = myq.popleft()

            if node.val >= maxVal:
                res += 1

            if node.left:
                myq.append((node.left, max(maxVal, node.val)))
            
            if node.right:
                myq.append((node.right, max(maxVal, node.val)))

        return res