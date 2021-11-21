class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # used_index = set()
        # res = []
        # for i in range(len(nums1)):
        #     for k in range(len(nums2)):
        #         if k in used_index:
        #             continue
        #         if nums1[i] == nums2[k]:
        #             used_index.add(k)
        #             res.append(nums2[k])
        #             break
        # return res
    
    #Time: O(n*m): n-num1; m-num2
    #Space: O(m): m-len(num2) 
    

        d_1 = get_dict(nums1)
        d_2 = get_dict(nums2)
        res_list = []
        for key in d_1.keys():    # O(n)
            if key in d_2.keys():
                val = min(d_1[key], d_2[key])  # O(1)
                for i in range(val):
                    res_list.append(key)  # O(1)
        return res_list
        # print("res_list",res_list)

        # Time: O(n+m) + O(n+m) = O(n+m)
        # Space: O(n+m) 
    
    
def get_dict(nums):  #Time: O(n)
    res={}
    for i in range(len(nums)):
        key = nums[i]
        if key in res.keys():
            res[key] += 1
        else:
            res[key] = 1
    return res
# print('dict',get_dict(nums2))