class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        for i in range(len(s)):
            if s[i].isalpha():
                letters.append(s[i])
            else:
                digits.append(s[i])

        if abs(len(letters) - len(digits)) > 1:
            return ("")
        res = []
        if len(letters) > len(digits):
            letters, digits = digits, letters
        if len(letters) < len(digits):
            res.append(digits.pop())    #O(1)

        for i in range(len(letters)): # O(N)
            res.append(letters[i])
            res.append(digits[i])
        return (''.join(res))

#Time: O(N) + O(1) + O(N) = O(N)
#Space: O(N)
        
    