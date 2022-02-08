# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def copy(head):
            copied_head = ListNode(-1)
            res = copied_head
            while head:
                copied_head.next = ListNode(head.val)
                copied_head = copied_head.next
                head = head.next
            return res.next
        
        def reverseList(head):

            def solver(node, prev_node):
                next_node = node.next   # delete to next node
                node.next = prev_node   # re-assign to new

                if not next_node:
                    return node
                return solver(next_node, node)

            return solver(head, None)
        
        reversed_ = reverseList(copy(head))
        # print (head)
        # print (reversed_)
        while head:
            if head.val != reversed_.val:
                return False
            head = head.next
            reversed_ = reversed_.next 
        return True
    