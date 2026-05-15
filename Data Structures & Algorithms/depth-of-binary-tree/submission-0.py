# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # stack = [[root, 1]]
        # res = 0

        # while stack:
        #     node, depth = stack.pop()
        #     print(stack, node, depth)
        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
            
        # return res

        if not root:
            return 0
        queue = deque([root])
        count = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(queue)
            count += 1
        
        return count
