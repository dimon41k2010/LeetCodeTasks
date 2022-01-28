class Solution:
    
    def isSameAfterReversals(self, num: int) -> bool:
        
        return num % 10 != 0 or num == 0     
        
# Time: O(1)
# Space: O(1)
