class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        def is_good(s):
            return s[0] == s[1] and s[0] == s[2]

        max_val = -1
        res = ""
        for i in range(0, len(num)-2):
            slice = num[i:i + 3]
            slice_val = int(slice)
            if is_good(slice) and max_val < slice_val:
                max_val = slice_val
                res = slice
        
        return (res)

#Time: O(N)
#Space: O(1)
        