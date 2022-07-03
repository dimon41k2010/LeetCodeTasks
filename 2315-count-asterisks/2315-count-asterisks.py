class Solution:
    def countAsterisks(self, s: str) -> int:
        
        # n_s = s.split("|")
        # count = 0
        # for i in range(0, len(n_s), 2):
        #     count += n_s[i].count("*")
        # return (count)
    
#Time: O(N)
#Space: O(N)

        res = 0 
        count_vertical_bar = 0 
        for char in s:
            if char == "|":
                count_vertical_bar += 1
            elif char == "*" and count_vertical_bar % 2 == 0:
                res += 1
        return res
    
#Time: O(N)
#Space: O(1)