class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        for i in range(len(s)): # O(n)
            n_s = s[i:] + s[:i]  # O(2*n)
            if n_s == goal:
                return (True)
        return (False)

# Time: O(n) * O(2*n) = O(n2)
# Space: O(n)