class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        left, right = 0, 100
        while left <= right:                # Time: O(log N)
            mid = (left + right) // 2
            special_num_candidate = mid
            count_special_nums = len( [num for num in nums if num >= special_num_candidate] )               # Time: O(N)
            # print(special_num_candidate, count_special_nums, "|", left, right)
            if special_num_candidate == count_special_nums:
                return(special_num_candidate)
            elif special_num_candidate < count_special_nums:
                left = mid + 1
            elif special_num_candidate > count_special_nums:
                right = mid - 1
        return (-1)

# Time: O(N) * O(log N) = O(N log N)
# Space: O(1)