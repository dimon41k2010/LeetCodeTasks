class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        counter = 0
        is_space = False
        
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                counter += 1
                is_space = True
            elif is_space:
                break
        return counter
    
#Time: O(n)
#Space: O(1)