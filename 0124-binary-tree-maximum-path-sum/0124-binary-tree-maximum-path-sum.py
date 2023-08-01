# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global answer
        answer = -1000
        
        def findMaxPath(node):
            if node == None: return 0
            leftPath = max(0, findMaxPath(node.left))
            rightPath = max(0, findMaxPath(node.right))
            
            global answer
            answer = max(answer, leftPath + rightPath + node.val)
            
            return node.val + max(leftPath, rightPath)
        
        
    
        
        findMaxPath(root)
        return answer
        