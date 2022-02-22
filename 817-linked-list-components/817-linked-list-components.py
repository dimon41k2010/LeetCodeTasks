# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        res = 0
        node = head
        nums_set = set(nums)
        
        while node:
            is_component = False
            while node and node.val in nums_set:
                is_component = True
                node = node.next
            if is_component:
                res += 1
            
            if node:
                node = node.next
        
        return res
    
# Time: O(N)
# Space: O(M) // M->len(nums)