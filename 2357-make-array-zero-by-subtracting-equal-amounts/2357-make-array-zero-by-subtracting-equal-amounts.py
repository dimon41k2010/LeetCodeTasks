class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        return(len(set([val for val in nums if val > 0])))

#Time: O(3 * N)
#Space: O(N)


        # set_nums = set(nums)  #O(N)
        # return(len(set_nums)-1 if 0 in set_nums else len(set_nums))  #O(1)

#Time: O(N)
#Space: O(N)
        