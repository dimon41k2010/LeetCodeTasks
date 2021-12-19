class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        def recur_v2(i, nums, res):
            # print("Enter",i, res)
            if i == len(nums):
                return

            if nums[i] % 2 == 0:
                res.append(nums[i])
            # print("Mid",i, nums[i], res)

            recur_v2(i + 1, nums, res)
            if nums[i] % 2 == 1:
                res.append(nums[i])
            # print("Exit",i, nums[i], res)

        result_2 = []
        recur_v2(0, nums, result_2)

        return(result_2)


#Time: O(N)
#Space: O(N)