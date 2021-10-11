class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
#         res = []
#         for i in range(len(s)):
#             if self.is_anagrams(p, s[i:len(p)+i]):
#                 res.append(i)
#         return res
    
    
#     def is_anagrams(self,a,b):
#         d={}
#         for i in a.lower():
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
#         for k in b.lower():
#             if k not in d.keys():
#                 return False
#             else:
#                 d[k] -= 1
#         for i in d.values():
#             if i != 0:
#                 return False

#         return True
    
#Time: O(s) * O(p) =  O(s*p)
#Space: O(n) // n = p


# ============================
        
        if len(p) > len(s):
            return []
        res = []
        count_p = [0 for _ in range(125)]
        count_sub_s = [0 for _ in range(125)]
        # print(s)
        for letter in p:
            count_p[ord(letter)] += 1
        for i in range(len(s)+1):
            if i < len(p):
                count_sub_s[ord(s[i])] += 1
            else:
                if is_equals(count_sub_s, count_p):
                    res.append(i-len(p))
                # print('added', s[i])
                if i < len(s):
                    count_sub_s[ord(s[i])] += 1
                    count_sub_s[ord(s[i - len(p)])] -= 1
                # print('deleted', s[i])
        return res
    
def is_equals(a,b):    #Time: O(1)   due to the limited 125 values in lists " count_p" and "count_sub_s"
    for i in range(len(a)):
        if b[i] != a[i]:
            return False
    return True

#Time: O(n)   a = 0-125 b = 0-125  
#Space: O(1)
