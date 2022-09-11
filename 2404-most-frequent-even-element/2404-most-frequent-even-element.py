class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        dic = Counter(nums)
        res = -1
        val = -1
        for key in dic.keys():
            key_val = dic[key]
            if key % 2 != 0:
                continue
            if key_val > val:
                val = key_val
                res = key
            elif key_val == val:
                res = min(res, key)
        return (res)

#Time: O(N)
#Space: O(N)