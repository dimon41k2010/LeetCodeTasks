# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = head
        # print (res.next)
        while head != None: 
            while head.next != None and head.val == head.next.val:
                 head.next  = head.next.next

            head = head.next 
        return res
    
# Time: O(N)
# Space: O(1)