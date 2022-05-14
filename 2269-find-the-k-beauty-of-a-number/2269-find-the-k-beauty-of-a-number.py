class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        module = 10 ** k
        temp_num = num
        res = 0
        while num >= module / 10:
            sub_str = num % module
            if sub_str and temp_num % sub_str == 0:
                res += 1
            num //= 10

        return res

#Time: O(N) // N=len(num)
#Space: O(1)