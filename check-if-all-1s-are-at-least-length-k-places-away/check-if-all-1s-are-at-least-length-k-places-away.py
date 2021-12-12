class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        dist = k
        for num in nums:
            if num == 0: 
                dist += 1
            elif dist >= k: 
                dist = 0
            else: 
                return False
        return True
    
#Time: O(N)
#Space: O(1)