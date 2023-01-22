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
            
            l, r = 0,0
            if node.left != None: l = dfs(node.left, curlen + 1)
            if node.right != None: r = dfs(node.right, curlen + 1)
                
            return max(l, r)
        
        return dfs(root, 1)
