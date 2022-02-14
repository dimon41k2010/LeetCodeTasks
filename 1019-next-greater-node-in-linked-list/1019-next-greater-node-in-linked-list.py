# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        def solver(node):
            
            if not node:
                return [], [0]
            
            rest_list, stack = solver(node.next)
            while stack and node.val >= stack[-1]:
                stack.pop()
            if not stack: 
                rest_list.append(0)
            else:
                rest_list.append(stack[-1])
            
            stack.append(node.val)
            
            return rest_list, stack
            
        res, _ = solver(head)
       
        return res[::-1]
        
        