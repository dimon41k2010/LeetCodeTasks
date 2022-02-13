class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr_point = self.head
        self.visit(homepage)
        
    def visit(self, url: str) -> None:
        next_node = self.tail
        new_node = ListNode(url)
        self.curr_point.next = new_node
        new_node.prev = self.curr_point
        new_node.next = next_node
        next_node.prev = new_node
        self.curr_point = new_node
        
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr_point.prev.val == self.head.val:
                break
            self.curr_point = self.curr_point.prev
        return self.curr_point.val
                
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr_point.next.val == self.tail.val:
                break
            self.curr_point = self.curr_point.next
        return self.curr_point.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)