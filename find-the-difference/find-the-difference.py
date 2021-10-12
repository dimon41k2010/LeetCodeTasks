class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        for letter in set(t):
            if s.count(letter) + 1 == t.count(letter):
                return letter

# Time: O(1) * O(n) = O(n)
# Space: O(26) = O(1)