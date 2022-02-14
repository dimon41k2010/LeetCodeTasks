class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        def recursion(num1, num2):
            
            if num1 == 0 or num2 == 0:
                return 0
            
            if num1 >= num2:
                num1 -= num2
            else: 
                num2 -= num1
            
            return recursion(num1, num2) + 1
        
        return recursion(num1, num2)
    
# Time: O(N)
# Space: O(N)