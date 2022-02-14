# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        def solver(node):
            
            if not node:
                return None, [0]
            
            rest_list, rest_max = solver(node.next)
            curr_node = None
            while rest_max and node.val >= rest_max[-1]:
                rest_max.pop()
            if not rest_max: 
                curr_node = ListNode(0, rest_list)
            else:
                curr_node = ListNode(rest_max[-1], rest_list)
            
            rest_max.append(node.val)
            
            return curr_node, rest_max
            
        res_link_list, _ = solver(head)
        res = []
        while res_link_list:
            res.append(res_link_list.val)
            res_link_list = res_link_list.next
        return res
        
        