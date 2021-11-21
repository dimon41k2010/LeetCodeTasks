class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #nums = [3,1,2,0,2,2,3,3,4,4]
        
        max_num = None
        second_max = None
        third_max = None

        for num in nums:
            if num == max_num or num == second_max or num == third_max:
                continue

            if max_num is None or max_num < num:
                third_max = second_max # 
                second_max = max_num  # 
                max_num = num # 3
            elif second_max is None or second_max < num: #
                third_max = second_max
                second_max = num
            elif third_max is None or third_max < num:
                third_max = num

        if third_max == None:
            return max_num

        return third_max
        
         #Time: O(n)
         #Space: O(1)         
        
     #====================   
#         nums.sort() #O(1)
#         res = nums[-1]
#         count = 2 #O(1)
#         for val in nums[::-1]:
#             if res > val:
#                 res = val 
#                 count -= 1 
#                 if count == 0:
#                     return res
                    
#         if count != 0:
#             return nums[-1]
        
        #Time: O(N log n) + O(n) = O(N log n)
        #Space: O(1) + O(1) + O(1) = O(1)