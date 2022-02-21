# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd_head = ListNode(-1)
        odd_tail = odd_head
        even_head = ListNode(-1)
        even_tail = even_head
        
        node = head
        index = 1
        while node:
            if index % 2 != 0:
                odd_tail.next = node
                odd_tail = odd_tail.next 
            elif index % 2 == 0:
                even_tail.next = node
                even_tail = even_tail.next
            
            node_next = node.next
            node.next = None
            node = node_next 
    
            index += 1
        
        odd_tail.next = even_head.next
        
        return odd_head.next
    
    
# Time: O(N)
# Space: O(1)