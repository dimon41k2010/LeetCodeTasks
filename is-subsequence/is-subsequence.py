class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True

        index = 0
        for letter in t:
            if letter == s[index]:
                index += 1
                if index == len(s):
                    return True
        
        return False

# Time: O(n) = O(n)
# Space: O(1) 