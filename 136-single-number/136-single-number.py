class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
                continue
            s.add(i)
        for i in s:
            return i
        return -1
    
#Time: O(n) * O(1)    | O(n) + O(N log n) + O(n^2)
#Space: O(n)