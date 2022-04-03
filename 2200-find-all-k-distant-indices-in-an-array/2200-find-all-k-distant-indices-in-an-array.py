class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        temp = []
        for i in range(len(nums)):
            if key == nums[i]:
                temp.append(i)
                
        res = []
        #first solution
        # j = 0
        # for i in range(len(nums)):
        #     while abs(i-temp[j]) > k:
        #         if i - temp[j] < 0:
        #             break
        #         j += 1
        #         if j > len(temp):
        #             print(res)
        #     else:
        #         res.append(i)
        # print(res)

        #second solution
        i = j = 0
        while i < len(nums) and j < len(temp):
            if abs(i - temp[j]) <= k:
                res.append(i)
                i += 1
            elif i - temp[j] < 0:
                i += 1
            elif i - temp[j] > 0:
                j += 1
        return (res)

# Time: O(N)
# Space: O(N)