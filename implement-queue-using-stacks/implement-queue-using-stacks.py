from queue import LifoQueue

class MyQueue:

    def __init__(self):
        self.stack = LifoQueue()

    def push(self, x: int) -> None:
        self.stack.put(x)

    def pop(self) -> int:
        temp_stack = LifoQueue()
        pop_val = None
        while not self.stack.empty():
            pop_val = self.stack.get()
            if not self.stack.empty():
                temp_stack.put(pop_val)

        while not temp_stack.empty():
            self.stack.put(temp_stack.get())

        return pop_val

    def peek(self) -> int:
        temp_stack = LifoQueue()
        pop_val = None

        while not self.stack.empty():
            pop_val = self.stack.get()
            temp_stack.put(pop_val)

        while not temp_stack.empty():
            self.stack.put(temp_stack.get())

        return pop_val

    def empty(self) -> bool:
        return self.stack.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()