# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        def solver(node, prev_node):
            next_node = node.next
            node.next = prev_node

            if not next_node:
                return node
            return solver(next_node, node)

        return solver(head, None)
    
# Time: O(N)
# Space: O(N)
