class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHashSet:
        
    
    def __init__(self):
        self.n = 100000
        self.array = [ None for i in range(self.n) ] 

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        hash_ = self.hash_code(key)
        head = self.array[hash_]
        
        self.array[hash_] = ListNode(key)
        self.array[hash_].next = head
        
    def remove(self, key: int) -> None:
        hash_ = self.hash_code(key)
        head = self.array[hash_]
        
        if head and head.val==key:
            self.array[hash_] = head.next 
            return 
        
        while head and head.next:
            if head.next.val == key:
                head.next = head.next.next
                return 
    
    def contains(self, key: int) -> bool:
        hash_ = self.hash_code(key)
        head = self.array[hash_]
        
        while head:
            if head.val == key:
                return True        
        
            head = head.next
        return False 
        
        
    def hash_code(self, key: int) -> int:
        return key % self.n
        
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)