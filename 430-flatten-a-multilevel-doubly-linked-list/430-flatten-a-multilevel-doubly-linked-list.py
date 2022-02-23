"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        node = head
        while node:      
            next_node = node.next
            
            if node.child:
                sub_head = self.flatten(node.child)
                sub_tail = sub_head
                while sub_tail.next:
                    sub_tail = sub_tail.next
                
                node.child = None
                node.next = sub_head
                sub_head.prev = node
                
                sub_tail.next = next_node
                if next_node:
                    next_node.prev = sub_tail
                
            node = next_node 
        
        return head