# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        
        remainings = length % k  # 3 % 5 = 3
        base_len = length // k  # 3 // 5 = 0
        res = []
        node = head
        for _ in range(k):
            if not node:
                res.append(None)
                continue
            len_ = base_len - 1 
            
            if remainings > 0: 
                len_ +=1
            
            res.append(node)
            for __ in range(len_):
                node = node.next
            node_next = node.next
            node.next = None
            node = node_next
            
            remainings -= 1
        
        return res