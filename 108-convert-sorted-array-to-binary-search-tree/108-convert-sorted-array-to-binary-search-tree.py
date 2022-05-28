# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recursion(left, right, nums):
            if left > right:
                return None
            
            middle = left + ((right + 1) - left) // 2 
           # print(middle, left, right)
            left_subtree = recursion(left, middle-1, nums)
            right_subtree = recursion(middle+1, right, nums)
            
            return TreeNode(val=nums[middle], left=left_subtree, right=right_subtree)
        
        return recursion(0, len(nums)-1, nums)
    
#Time: O(N)
#Space: O(Log N)
