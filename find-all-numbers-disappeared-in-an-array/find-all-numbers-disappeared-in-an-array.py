class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_s = set(nums)
        res_2 = []
        for i in range(1, len(nums)+1): 
            if i not in new_s:
                res_2.append(i)
        
        return res_2
    
#Time: O(n)
#Space: O(n)