class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        count_dict = {}         #Time/Space: O(N)
        for num in nums:
            if num not in count_dict.keys():
                count_dict[num] = 1
            else:
                count_dict[num] += 1
  
    # option 1
        # for value in count_dict.values():  #Time/Space: O(N)
        #     if value % 2 != 0:
        #         print(False)
        # print(True)
    
    # option 2
        return (len( [  value for value in count_dict.values() if value % 2 == 1 ]) == 0 ) #Time/Space: O(N)

# Time: O(N)
# Space: O(N)