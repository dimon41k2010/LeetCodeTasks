class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):   #O(N)
            while nums[i] - 1 != i:
                if nums[nums[i]-1] == nums[i]:
                    break
                i_1 = i         # for correct swapping use extra variable !  O(1)
                i_2 = nums[i]-1 # for correct swapping use extra variable !  O(1)

                temp = nums[i_1]
                nums[i_1] = nums[i_2]
                nums[i_2] = temp
                # nums[i_1], nums[i_2] = nums[i_2], nums[i_1]
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return(nums[i], i+1)

#Time: O(N)
#Space: O(1)