class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        for letter in set(s):  #O(26)
            left = 0
            right = len(s)-1
            while left < len(s)-1:    #O(N)
                if s[left] == letter:
                    break
                left += 1
            while right >= 0:       #O(N)
                if s[right] == letter:
                    break
                right -= 1

            distance = right - left - 1
            res = max(distance, res)
        return (res)

#Time: O(26) * O(N) = O(N)
#Space: O(1)
        
        
    
    