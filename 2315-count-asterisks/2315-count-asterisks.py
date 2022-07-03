class Solution:
    def countAsterisks(self, s: str) -> int:
        
        n_s = s.split("|")
        count = 0
        for i in range(0, len(n_s), 2):
            count += n_s[i].count("*")
        return (count)
    
#Time: O(N)
#Space: O(N)
