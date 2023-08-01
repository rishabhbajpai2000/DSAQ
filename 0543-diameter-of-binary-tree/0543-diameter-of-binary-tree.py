# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global diameter
        diameter = 0
        
        def height(node):
            if node == None: return 0
            lh = height(node.left)
            rh = height(node.right)
            
            global diameter
            diameter = max(diameter, lh + rh)
            return 1 + max(lh,rh) 
        
        
        height(root)
        return diameter
