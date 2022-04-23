class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        candidate = min([abs(num) for num in nums ])
        return (candidate if candidate in nums else -candidate)


# Time: O(N)
# Space: O(N)