class Solution:
    def pivotIndex(self, nums: List[int]) -> int:  ## [1,7,3,6,5,6]
#         n = len(nums)
#         for i in range(0, n):
            
#             sum_l = self.sum(nums, 0, i)
#             sum_r = self.sum(nums, i+1, n)
        
#             if sum_l == sum_r:
#                 return i
             
#         return -1
    
#     def sum(self, nums, l, r): #l=0 r=3 res = 11
#         result = 0
#         for i in range(l, r):
#             result += nums[i]
            
#         return result
        
# second solution
        
        n = len(nums)                                           
        sum_list = []                             
        sum_list.append(0)
        for i in range(0, n):                      # O(n)
            sum_list.append(sum_list[i] + nums[i])

        for i in range(0, n):                      # O(n)
            sum_l = sum_list[i]
            sum_r = sum_list[n] - sum_list[i + 1] 
            if sum_l == sum_r:
                return i
             
        return -1
    
    # Time: O(n)
    # Space: O(1)