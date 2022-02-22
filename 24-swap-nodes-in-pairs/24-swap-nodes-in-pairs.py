# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode(-1, head)
        res = node      
        
        while node and node.next and node.next.next:
            prev_node = node
            current_node = node.next
            next_node = node.next.next
            next_next_node = node.next.next.next
            
            prev_node.next = next_node
            current_node.next = next_next_node
            next_node.next = current_node
            
            node = current_node
               
        return res.next
    