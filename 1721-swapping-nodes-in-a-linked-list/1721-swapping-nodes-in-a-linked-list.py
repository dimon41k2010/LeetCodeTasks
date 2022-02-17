# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head.next:
            return head
        node = head
        lenght = 0
        while node:
            lenght += 1
            node = node.next
            
        first_idx = k - 1 # first_idx_prev
        second_idx = lenght - k # second_idx_prev
        if first_idx > second_idx:
            first_idx, second_idx = second_idx, first_idx
        
        first_node_prev = None
        second_node_prev = None
        index = 1
        
        node = head
        while node:
            if index == first_idx:
                first_node_prev = node
            if index == second_idx:
                second_node_prev = node
            index += 1
            node = node.next
        
        if first_idx == 0:
            second_node = second_node_prev.next 
            second_node_prev.next = head
            second_node.next = head.next
            head.next = None
            head = second_node
        elif first_idx + 1 == second_idx:
            first_node = first_node_prev.next
            second_node = second_node_prev.next 
            second_node_next = second_node.next
            first_node_prev.next = second_node
            second_node.next = first_node
            first_node.next = second_node_next
        elif first_idx == second_idx:
            pass
        else:
            first_node = first_node_prev.next
            second_node = second_node_prev.next 
            
            first_node_next = first_node.next
            second_node_next = second_node.next
            
            first_node_prev.next = second_node
            second_node.next = first_node_next
            second_node_prev.next = first_node
            first_node.next = second_node_next
            
        return head
    
            
            
            
            
          #  
        # print(first_node)
        # print(second_node)       