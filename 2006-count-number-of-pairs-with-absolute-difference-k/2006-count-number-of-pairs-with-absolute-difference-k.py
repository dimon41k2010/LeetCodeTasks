class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        dic = Counter(nums)
        
        def get_pairs(dic, op):
            res = 0
            for num in nums:
                key = op(num, k)
                if key in dic.keys():
                    res += dic[key]
                    print(num,key,dic[key])
            return res

        return(get_pairs(dic, lambda a,b: a+b))

#Time: O(N)
#Space: O(N)