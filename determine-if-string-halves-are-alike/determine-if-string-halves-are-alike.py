class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0
        for i in range(len(s)//2): 
            if s[i] in vowels:
                count += 1
            if s[i+(len(s)//2)] in vowels:
                count -= 1
        if count != 0:
            return (False)
        return (True)

#Time: O(N)
#Space: O(1) + O(10)