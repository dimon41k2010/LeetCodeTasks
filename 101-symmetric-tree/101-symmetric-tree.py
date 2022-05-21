# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        
        return self.recursive(root, root)
    
    def recursive(self, left, right):
    
        if left == None or right == None:
            return left == right
        if left.val != right.val:
            return False
        else:
            return left.val == right.val and self.recursive(left.left, right.right) and self.recursive(left.right, right.left)