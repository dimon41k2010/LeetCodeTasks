class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # print(len(nums) + 1 - k)
        # res = None
        # range_end = len(nums) + 1 - k
        # for i in range(range_end):      # Time: O(N)
        #     window = nums[i:i+k]        # Time: O(K)
        #     print(window)
        #     average = sum(window) / k
        #     if not res or res < average:
        #         res = average
        # 
        # return(res)

        # Time: O(N * K) = O(N^2)
        # Space: O(K) K = len(window)

        # =======================
                    
        res = None
        sum_ = 0
        for i in range(len(nums)):      # Time: O(N)
            if i < k:
                sum_ += nums[i]
                continue
            average = sum_ / k
            if not res or res < average:
                res = average
            sum_ += nums[i]
            sum_ -= nums[i-k]
        if res == None:
            return sum_ / k
        return (max(res, sum_ / k))

# Time: O(N)
# Space: O(1)