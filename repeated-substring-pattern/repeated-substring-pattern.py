class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        max_sub = len(s)//2

        for i in range(0, max_sub):     # O(n)
            if len(s) % (i+1) == 0:  
                substr = s[0:i+1]
                if is_built(s, substr):  # O(n)
                    return  True
        return False


def is_built(s,substr):   # O(n)
    index = 0
    for letter in s:
        if letter != substr[index]:
            return False
        index += 1
        if index == len(substr):
            index = 0
    return True


# Time: O(n) * O(n) = O(n2) // n=len(s)
# Space: O(n) // n=len(s)