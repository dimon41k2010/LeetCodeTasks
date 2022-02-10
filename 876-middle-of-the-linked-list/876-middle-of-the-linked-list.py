# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next: 
            
            fast = fast.next.next
            slow = slow.next
        
#         if not fast: 
#             return slow.next
        
#         elif not fast.next: 
#             return slow
        
        return slow
# Time: O(N/2) = O(N)
# Space: O(1)
