class Solution:
    def checkString(self, s: str) -> bool:
 # Solution 1      
        is_b = False
        for char in s:
            if char == "b":
                is_b = True
            elif is_b == True and char == "a":
                return False
        return True
    
# Time: O(N)
# Space: O(1)

 # Solution 2
        for i in range(1,len(s)):
            if s[i-1] == 'b' and s[i] == 'a':
                return False
        return True
    
# Time: O(N)
# Space: O(1)

 # Solution 3
        return all([ not (s[i-1] == 'b' and s[i] == 'a') for i in range(1,len(s)) ])
# Time: O(N)
# Space: O(N)