# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:   
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            self.result=max(self.result, l+r)

            return max(l, r) + 1

        dfs(root)

        return self.result
