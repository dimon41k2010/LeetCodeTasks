class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
#         current_level = set([''])
#         while n > 0:
#             next_level = set()
#             for combination in current_level:
#                 next_level.add("()" + combination)
#                 next_level.add(combination + "()")
#                 next_level.add("(" + combination + ")")
#             current_level = next_level
#             n -= 1

#         return(list(current_level))

#Time: O(N^3)
#Space: O(N^3) => O(1)

        # improoved solution.
    
        res = []
        s = [("(", 1, 0)]
        while s:
            x, l, r = s.pop()
            if l - r < 0 or l > n or r > n:
                continue
            if l == n and r == n:
                res.append(x)
            s.append((x+"(", l+1, r))
            s.append((x+")", l, r+1))
        return res