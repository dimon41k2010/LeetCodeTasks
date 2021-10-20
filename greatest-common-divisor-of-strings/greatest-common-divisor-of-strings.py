class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        min_str = min(len(str2), len(str1))  #O(1)
        res = ''
        for i in range(1, min_str+1):  #O(N)
            if len(str1) % i == 0 and len(str2) % i == 0:
                divider = str1[0:i]  #O(N)
                if divider * (len(str1) // i) == str1 and divider * (len(str2) // i) == str2:  # O(N)
                    res = divider
        return res

#Time: O(1) + O(N) * O(N) = O(N^2)
#Space: O(N) 