# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        
        def dfs(node, curlen):
            if node.left == None and node.right == None:
                return curlen
            
            l = 0 if node.left == None else dfs(node.left, curlen + 1)
            r = 0 if node.right == None else dfs(node.right, curlen + 1)
                
            return max(l, r)
        
        return dfs(root, 1)
