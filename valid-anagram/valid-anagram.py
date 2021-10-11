class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        n_s = sorted(s)
        n_t = sorted(t)
        
        for i in range(len(s)):
            if n_s[i] != n_t[i]:
                return False

        return True
    
# Time: O(N log N) + O(n) = O(N log N)
#Space: O(s + t) 