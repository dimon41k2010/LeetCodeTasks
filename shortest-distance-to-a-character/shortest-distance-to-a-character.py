class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        for i in range (len(s)): 
            left_inx = i
            right_inx = i
            count = 0  
            while left_inx >= 0 or right_inx < len(s):
                if left_inx < 0:
                    pass
                else:
                    if s[left_inx] == c:
                        res.append(count)
                        break
                    else: 
                        left_inx -= 1
                
                if right_inx >= len(s):
                    pass
                else:
                    if s[right_inx] == c:
                        res.append(count)
                        break
                    else: 
                        right_inx += 1
                count += 1
        return res