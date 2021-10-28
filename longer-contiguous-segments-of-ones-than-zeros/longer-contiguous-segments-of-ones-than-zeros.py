class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count_0 = 0
        count_1 = 0
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and s[i] == s[start]:
                i += 1
            if s[start] == "1":
                count_1 = max(count_1, i - start)  #len(s[start:i])
            else:
                count_0 = max(count_0, i - start)
        return (count_1 > count_0)

#Time: O(N)
#Space: O(1)