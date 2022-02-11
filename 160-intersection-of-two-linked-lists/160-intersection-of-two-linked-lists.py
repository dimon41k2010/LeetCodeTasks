# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        def lenght(head):   # Time:O(N+M)
            res = 0 
            while head:
                res += 1
                head = head.next
            return res
        # print (lenght(headB))
        lenght_a = lenght(headA)
        lenght_b = lenght(headB)
        
        if lenght_a < lenght_b:     # Time:O(1)
            headA, headB = headB, headA
            lenght_a, lenght_b = lenght_b, lenght_a
        
        skip = lenght_a - lenght_b
        for _ in range(skip):        # Time:O(N+M)
            headA = headA.next
        
        # print(headA)
        # print(headB)
        
        while headA:     # Time:O(N+M)
            if headA.__hash__() == headB.__hash__():
                return headA
            
            headA = headA.next
            headB = headB.next
            
            
# Time: O(N+M) // N->headA, M->headB
# Space: O(1)
        