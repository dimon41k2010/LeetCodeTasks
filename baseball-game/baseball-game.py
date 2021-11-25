from queue import LifoQueue

def is_numb(operation):  # Time: O(1)
    try:
        int(operation)
        return True
    except:
        return False

class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stack = LifoQueue()

        for operation in ops:        #Time: O(N)
            if is_numb(operation):
                stack.put(int(operation))

            elif operation == "C":
                stack.get()
            elif operation == "D":
                val = stack.get()
                stack.put(val)
                stack.put(val * 2)
            elif operation == "+":
                val1 = stack.get()
                val2 = stack.get()

                stack.put(val2)
                stack.put(val1)
                stack.put(val1 + val2)
        res_sum = 0
        while not stack.empty():   #Time: O(N)
            res_sum += stack.get()
        return res_sum
         
        
# Time: O(N)
# Space: O(N)
        
    