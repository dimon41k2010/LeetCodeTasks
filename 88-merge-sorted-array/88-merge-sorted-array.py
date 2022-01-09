class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        index = (m + n) -1
        i_1 = m - 1
        i_2 = n - 1
        # nums1 = [1,2,3,0,0,0] m = 3,
        # nums2 = [6,7,8] n = 3
        
        for index in range(len(nums1)-1, -1,-1):
           # print(i_1, i_2)
            if i_1 == -1:
                nums1[index] = nums2[i_2]
                i_2 += -1
            elif i_2 == -1:
                nums1[index] = nums1[i_1]
                i_1 += -1
            
            elif nums1[i_1] < nums2[i_2]:
                nums1[index] = nums2[i_2]
                i_2 += -1
            elif nums1[i_1] >= nums2[i_2]:
                nums1[index] = nums1[i_1]
                i_1 += -1

            
        #Time: O(m+n) n = 3, m = 6
        #Space: O(1)