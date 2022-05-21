# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
            
class Solution:    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []
        
        def recursion(node):
            if not node:
                return
            
            recursion(node.left)
            self.res.append(node.val)
            recursion(node.right)
        
        recursion(root)
        
        return self.res
    
    
#Time: O(N)
#Space: O(N)