# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.simple_list = []
        while head:
            self.simple_list.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.simple_list)-1)
        return self.simple_list[random_index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Time: O(C) // C -> # of calls 
# Space: O(N)