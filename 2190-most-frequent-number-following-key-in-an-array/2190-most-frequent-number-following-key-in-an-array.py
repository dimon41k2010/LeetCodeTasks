class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        d = {}
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] not in d.keys():
                    d[nums[i+1]] = 1
                else:
                    d[nums[i+1]] += 1
                    
        res = -1
        count = -1
        for key in d.keys():
            if d[key] > count:
                count = d[key]
                res = key
        
        return(res)

#Time: O(N)
#Space: O(N)
      
    
# with list comprehension
        # from collections import Counter

        d = Counter([ nums[i+1]  for i in range(len(nums)-1) if nums[i] == key ])
        res = -1
        count = -1
        for key in d.keys():
            if d[key] > count:
                count = d[key]
                res = key
        return(res)

#Time: O(N)
#Space: O(N)