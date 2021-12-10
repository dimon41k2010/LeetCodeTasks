class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        start_value = 1
        
        def check(start_value, nums):
            temp = start_value
            for num in nums:
                temp += num
                if temp < 1:
                    return False
            return True
        
        while start_value:
            if check(start_value, nums):
                return start_value
            start_value += 1
    
    
# Time: O(N^2)
# Space: O(1)