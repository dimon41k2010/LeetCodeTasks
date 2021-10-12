class Solution:
    def firstUniqChar(self, s: str) -> int:

#         res = len(s)
#         for i in set(s): # O(26)
#             if s.count(i) == 1:  # O(n)
#                 res = min(res, s.index(i))   

#         if res == len(s): 
#             return -1
#         else:
#             return res

# Time: O(n)
# Space: O(26) = O(1)


#Second method with dictionary
        d = {}
        set1 = set()
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1

        for key in d.keys():
            if d[key] == 1:
                set1.add(key)
        if len(set1) == 0:
            return -1

        res2 = 0
        for val in s:
            if val in set1:
                res2 = s.index(val)
                break
        return res2
        
# Time: O(n) + O(1) + O(n+m) = O(n)
# Space: O(26) + O(26) = O(1)