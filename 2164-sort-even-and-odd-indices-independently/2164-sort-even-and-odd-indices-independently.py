class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        odd = []
        even = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        even.sort()
        even.reverse()
        odd.sort()
        res = []
        while odd or even:
            res.append(even.pop())
            if odd:
                res.append(odd.pop())
        return (res)

# Time: O(N) + O(N log N) + O(N) = O(N log N)
# Space: O(N) 
