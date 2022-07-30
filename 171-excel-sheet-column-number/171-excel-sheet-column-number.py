class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        res = 0
        for i, letter in enumerate(reversed(columnTitle)):
            letter_index = ord(letter) - ord("A") + 1
            res += 26 ** i * letter_index
        return (res)
    
#Time: O(N)
#Space: O(1)