class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            temp = list(nums)
            temp.pop(i)
            if temp == sorted(temp) and len(temp) == len(set(temp)):
                return (True)
            
        return(False)