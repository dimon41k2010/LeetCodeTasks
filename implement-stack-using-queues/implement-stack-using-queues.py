import queue

class MyStack:

    def __init__(self):
        self.q = queue.Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        temp_q = queue.Queue()
        val = None
        while not self.q.empty():
            val = self.q.get()
            if not self.q.empty():
                temp_q.put(val)
        self.q = temp_q
        return val

    def top(self) -> int:
        temp_q = queue.Queue()
        val = None
        while not self.q.empty():
            val = self.q.get()
            temp_q.put(val)
        self.q = temp_q
        return val

    def empty(self) -> bool:
        return self.q.empty()
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()