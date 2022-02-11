class ListNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

        
class MyHashMap:

    def __init__(self):
        self.n = 100000
        self.array = [ None for i in range(self.n) ]

        
    def put(self, key: int, value: int) -> None:
        hash_ = self.hash_code(key)
        head = self.array[hash_]
        
        if self.get(key) != -1:
            while head:
                if head.key == key:
                    head.value = value  
                    return
                head = head.next
        
        else: 
            self.array[hash_] = ListNode(key,value)
            self.array[hash_].next = head
            

    def get(self, key: int) -> int:
        hash_ = self.hash_code(key)
        head = self.array[hash_]
        
        while head:
            if head.key == key:
                return head.value       
        
            head = head.next
        return -1 
        
        
    def remove(self, key: int) -> None:
        hash_ = self.hash_code(key)
        head = self.array[hash_]
        
        if head and head.key == key:
            self.array[hash_] = head.next 
            return 
        
        while head and head.next:
            if head.next.key == key:
                head.next = head.next.next
                return 
        
        
    def hash_code(self, key: int) -> int:
        return key % self.n

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)