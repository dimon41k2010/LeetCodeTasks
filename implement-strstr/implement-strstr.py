class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
    # if needle is empty
        if needle == "":
            return '0'

        l = len(needle)
        res = -1
        for i in range(len(haystack)):
            if haystack[i:i+l] == needle:
                res = i
                break
        return res
    
#Time: O(n) * O(m) = O(n*m)  // m = len(needle)
#Space: O(1)
        
    
# #2 :Second solution], but very slow one with extra memory.
#         if needle == "":
#             return '0'

#         l = len(needle)
#         d ={}
        
#         for i in range(len(haystack)-1,-1,-1):
#             d[haystack[i:i+l]] = i
#         if needle in d.keys():
#             return d[needle]
#         return -1

#Time: O(n) * O(m) = O(n*m)  // m = len(needle)
#Space: O(n) n = len(haystack) 