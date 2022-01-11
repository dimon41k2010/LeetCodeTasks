class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replace_index = 0

        for current_index in range(0, len(nums)):
            if val != nums[current_index]:
                nums[replace_index] = nums[current_index]
                replace_index += 1  
        for i in range(replace_index, len(nums)):
            nums[i] = "_"
        return replace_index
    
    #Time: O(n) + O(n)
    #Space: O(1)