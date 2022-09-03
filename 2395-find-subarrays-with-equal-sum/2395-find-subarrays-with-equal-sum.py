class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sub_arr_dic = {}
        sum_sub = 0
        for i in range(0,len(nums)-1):
            sum_sub = nums[i] + nums[i+1]
            if sum_sub not in sub_arr_dic.keys():
                sub_arr_dic[sum_sub] = i
            else:
                return(True)
        return (False)
    
#Time: O(N)
#Space: O(N)