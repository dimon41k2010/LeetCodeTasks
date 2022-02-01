class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        nums_sub = sorted(nums)
        nums_sub = nums_sub[len(nums_sub) - k:]
        count_d = {}
        for num in nums_sub:
            if num in count_d:
                count_d[num] += 1
            else:
                count_d[num] = 1
        res = []
        for val in nums:
            if val in count_d.keys() and count_d[val] > 0:
                res.append(val)
                count_d[val] -= 1
        
        return res

# Time: O(N log N) + O(K) + O(N) = O(N log N)
# Space: O(N) + O(K) + O(K) = O(N)
        
