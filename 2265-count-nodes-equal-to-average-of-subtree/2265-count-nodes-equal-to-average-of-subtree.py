# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        def helper(node):
            
            if node == None:
                return 0,0
            
            left_sum, left_count = helper(node.left)
            right_sum, right_count = helper(node.right)
            
            cur_sum = left_sum + right_sum + node.val
            cur_count = left_count + right_count + 1 
            
            if cur_sum // cur_count == node.val:
                self.res += 1
            
            return cur_sum, cur_count
        
        helper(root)
        return self.res
        
#Depth-first search
    
    
#Time: O(N)
#Space: O(N)