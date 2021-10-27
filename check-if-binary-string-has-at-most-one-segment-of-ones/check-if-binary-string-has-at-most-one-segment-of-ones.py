class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] == "1" and s[i-1]== "0":
                return (False)
        return True

#Time: O(N)
#Space: O(1)
        
        