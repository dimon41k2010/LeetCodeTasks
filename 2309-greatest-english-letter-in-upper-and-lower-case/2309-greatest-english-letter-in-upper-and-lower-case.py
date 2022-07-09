class Solution:
    def greatestLetter(self, s: str) -> str:
        
        unique_letters = set(s)
        res = ""
        for char in s:
            if char.lower() in unique_letters and char.upper() in unique_letters:
                res = max(res, char.upper())
        return (res)

        
#Time: O(N)
#Space: O(26)