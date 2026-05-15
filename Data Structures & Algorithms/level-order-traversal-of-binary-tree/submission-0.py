# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        myq = deque([root])
        res = []

        while myq:
            currentLevel = []
            for i in range(len(myq)):
                node = myq.popleft()
                if node.left:
                    myq.append(node.left)
                if node.right:
                    myq.append(node.right)
                currentLevel.append(node.val)
            res.append(currentLevel)
        
        return res