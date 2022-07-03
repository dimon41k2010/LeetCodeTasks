class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return(ans)

        #return([nums[nums[i]] for i in range(len(nums))])

#Time: O(N)
#Space: O(1)