class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            temp = list(nums)
            temp.pop(i)
            if temp == sorted(temp) and len(temp) == len(set(temp)):
                return (True)
            
        return(False)
    
    
# Time: O(N^2) -> due to temp list creation on every iteration 
# Space: O(N + M)