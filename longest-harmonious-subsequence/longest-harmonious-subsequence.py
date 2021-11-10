class Solution:
    def findLHS(self, nums: List[int]) -> int:
#         nums_set = list(set(nums))
#         nums_set.sort()   #Time: O(N log n) 
#         # print(nums_set)
#         res = 0
#         for i in range(1,len(nums_set)):  #Time: O(n) 
#             min_ = nums_set[i-1]
#             max_ = nums_set[i]
#             if min_ + 1 != max_:
#                 continue
#             count = nums.count(min_) + nums.count(max_) #Time: O(2n) -> O(n) 
#             res = max(res, count)

#         return res
    
    # Time: O(n2)
    # Space: O(n)
    
    #================
    
        count_dict = {}   
        for num in nums:
            if num in count_dict.keys():
                count_dict[num] += 1
            else:
                count_dict[num] = 1
                
        nums_set = list(set(nums))
        nums_set.sort() #Time: O(N log n)
        # print(nums_set)
        res = 0
        for i in range(1,len(nums_set)): #Time: O(n)
            min_ = nums_set[i-1]
            max_ = nums_set[i]
            if min_ + 1 != max_:
                continue
            count = count_dict[min_] + count_dict[max_] #Time: O(2n) -> O(n)
            res = max(res, count)

        return res
    
    # Time: O(n)
    # Space: O(n)