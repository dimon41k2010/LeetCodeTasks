class Solution:
    def convertToTitle(self, num: int) -> str:

    # 1000 = 10 ^ 3 * (1)   + 10 ^ 2 * (0)  + 10 ^ 1 * (0) + 10 ^ 0 * (0)
    # 1000 = 26 ^ 2 * (1) + 26 ^ 1 * (12) + 26 ^ 0 * (12)
                                                 # L
    # 38 = 26 ^ 1 * (1) + 26 ^ 0 * (12)       12
                                    # L
    # 1 = 26 ^ 0 * (1) 
               # A
                                            
    # 1000 = 26 * 26 + 26 * 12 + 12
        textin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        if num == 1:
            return textin[0]
        
        res = ""
        while num > 0:
            i = num % 26
            res += str(textin[i - 1])
            num = (num - 1) // 26
        return res[::-1]