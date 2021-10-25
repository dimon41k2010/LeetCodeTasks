class Solution:
    def maxDepth(self, s: str) -> int:
        
        counter = 0
        res = 0
        for char in s:
            if char == "(":
                counter +=1
            elif char == ")":
                counter -=1
            if res < counter:
                res = counter
        return (res)

#Time: O(N)
#Space: O(1)
        
      
    