# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        res = list1
        index_node = 0
        while index_node+1 < a:
            index_node += 1
            list1 = list1.next
        # print(list1, index_node)
        
        while index_node+1 >= a and index_node+1 <= b:
            list1.next = list1.next.next
            index_node += 1
        # print(list1)
        
        next_node = list1.next
        list1.next = list2
        while list1.next:
            list1 = list1.next
        list1.next = next_node
        
        return res
            