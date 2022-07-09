# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def rec(node):
            
            if not node.left and not node.right:
                return node.val == 1
            
            left_res = rec(node.left)
            right_res = rec(node.right)
            
            if node.val == 2:
                
                return left_res or right_res
            return left_res and right_res
        
        return rec(root)
        
        
#Time: O(N)
#Space: O(N)

        
        