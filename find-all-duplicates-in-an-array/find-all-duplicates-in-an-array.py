class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # n_s = set(nums)
        # res = []
        # for val in nums:
        #     if val in n_s:
        #         n_s.remove(val)
        #     else:
        #         res.append(val)
        # return res
    #Time: O(n)
    #Space: O(n)
    #============
        
        result = []
        for i in range(len(nums)):
            while nums[nums[i]-1] != nums[i]:
                # print(nums)
                # print([x for x in range( len(nums))])
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                # print(i)
                # print(nums)
                # print("============")

        for i in range(len(nums)):
            if i+1 != nums[i]:
                # print("i:",i)
                result.append(nums[i])
        return result

    #Time: O(2n) = O(n)
    #Space: O(1)