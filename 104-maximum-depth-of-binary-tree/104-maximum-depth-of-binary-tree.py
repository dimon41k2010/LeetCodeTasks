# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
#         res = 0
#         if root == None:
#             return res
    
#         if root.left != None or root.right != None:
#             res += 1
        
#         print(self.maxDepth(root.left))
#         print(self.maxDepth(root.right))
        
#         return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))
        
        #------
        if root == None:
            return 0
        
        queue = []
        queue.append(root)
        res = 0
        
        while len(queue) != 0:
            next_level_queue = []
            for node in queue:
                if node.left:
                    next_level_queue.append(node.left)
                if node.right:
                    next_level_queue.append(node.right)
            
            queue = next_level_queue
            res += 1
            # print([node.val for node in next_level_queue])
        return res