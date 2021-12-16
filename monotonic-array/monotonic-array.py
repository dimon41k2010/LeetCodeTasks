class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        def is_sorted_inc_recur(i, nums):
            # print("Enter:", i)
            if i == len(nums):
                return True
            # print("Val:", i, nums[i])
            if nums[i-1] <= nums[i]:
                next_return = is_sorted_inc_recur(i+1, nums)
                # print("next_return", next_return, i)
                return next_return
            else:
                return False
        # print(is_sorted_inc_recur(1,nums))

        def is_sorted_dec_recur(i, nums):
            if i == len(nums):
                return True

            if nums[i-1] >= nums[i]:
                next_return = is_sorted_dec_recur(i+1, nums)
                return next_return
            else:
                return False

        return (is_sorted_inc_recur(1, nums) or is_sorted_dec_recur(1, nums)) #Space: O(2*N)

    
    
#Time: O(N)
#Space: O(2*N) => O(N)