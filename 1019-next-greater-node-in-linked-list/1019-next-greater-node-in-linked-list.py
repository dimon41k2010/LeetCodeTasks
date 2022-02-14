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
            
            rest_list, rest_max = solver(node.next)
            while rest_max and node.val >= rest_max[-1]:
                rest_max.pop()
            if not rest_max: 
                rest_list.append(0)
            else:
                rest_list.append(rest_max[-1])
            
            rest_max.append(node.val)
            
            return rest_list, rest_max
            
        res_link_list, _ = solver(head)
       
        return res_link_list[::-1]
        
        