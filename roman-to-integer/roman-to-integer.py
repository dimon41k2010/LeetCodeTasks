class Solution:
    def romanToInt(self, s: str) -> int:
#         3999 == "MMM CM XC IX"
#         M M M =     3
#           C M      100 - 1000   
#           X C     10 - 100
#           I X      1 - 10
            
#         1 - 6
        
#         I   II  III    IV   V   VI  VII VIII    IX   X
#         VI VII VIII    IX   X
        
#         symbols = I, V, X, L, C, D, M
#         s = "M C M X C I V"
        
#         res = 104 - 10 = 1000 + 94 - 100 = 994 + 1000

        numerals = {"I": 1,"V":5,"X":10, "L": 50, "C" : 100, "D":500, "M":1000}

        res = 0

        for i in range(len(s)-1,-1,-1):
            if i == len(s)-1 or numerals[s[i]] >= numerals[s[i+1]]:
                res += numerals[s[i]]
            elif numerals[s[i]] < numerals[s[i+1]]:
                res -= numerals[s[i]]
        return res
    
#Time: O(n)
#Space: O(1)