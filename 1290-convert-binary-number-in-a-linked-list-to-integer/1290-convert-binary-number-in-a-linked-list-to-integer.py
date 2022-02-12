# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        new_head = None
        prev_node = None
        while head:
            next_node = head.next   # delete to next node
            head.next = prev_node
            prev_node = head
            head = next_node
        
        power = 0  
        head = prev_node
        res = 0
        while head:
            res += head.val *(2**power) 
            power += 1    
            head = head.next
            # print(res)
        return res
        # print(prev_node)
            