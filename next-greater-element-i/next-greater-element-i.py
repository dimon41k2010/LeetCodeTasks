class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for val in nums1:
            index_nums2 = nums2.index(val)
            is_found = False
            for i in range(index_nums2, len(nums2)):
                if nums2[i] > val:
                    is_found = True
                    res.append(nums2[i])
                    break
            if not is_found:
                res.append(-1)
           
        return res
    
    
    
    
    
   


    #Time: O(n) + O(1) * O(m) = O(n*m)
    #Space: O(1)