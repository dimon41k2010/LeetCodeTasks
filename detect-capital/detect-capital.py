class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
#         for char in word:
#             if char != char.upper():
#                 return (False)
#         return (True)
        
#         for i in range(1, len(word)):
#             if word[i] == word[i].lower():
#                 return (False)
#         return (True)
        
        if word.isupper() or word.islower() or word[0].isupper() and word[1:].islower():
            return True
    
# Time: O(n) + O(n) = O(n)
# Space: O(1)