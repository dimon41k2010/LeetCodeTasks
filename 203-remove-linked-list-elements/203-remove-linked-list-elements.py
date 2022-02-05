# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        res = head
        while head and head.next:
            while head.next and val == head.next.val:
                head.next = head.next.next
           
            head = head.next
        
        if res.val == val:
            return res.next
        return res
    
# Time: O(N)
# Space: O(N)
