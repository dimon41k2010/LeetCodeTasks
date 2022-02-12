# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast = head
        new_head = None
        prev_node = None
        
        while fast:
            fast = fast.next.next
            next_node = head.next   # delete to next node
            head.next = prev_node   # re-assign to new
            prev_node = head
            head = next_node
        
        # print(head)   
        # print(prev_node)
        res = 0
        while head:
            res = max(head.val + prev_node.val, res)
            
            head = head.next
            prev_node = prev_node.next
        
        return res