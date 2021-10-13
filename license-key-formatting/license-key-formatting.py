class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
       
        res_list = []
        group_count = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] == "-":
                pass
            else:
                res_list.append(s[i].upper())    # O(1)
                group_count += 1
                if group_count == k:
                    res_list.append("-")
                    group_count = 0
        if len(res_list) == 0:
            return ""
        if res_list[len(res_list)-1] == "-":
            res_list.pop()
        
        return "".join(res_list[::-1])  #O(n) join + O(n) - reverse

# Time: O(n) + O(n) = O(n)
# Space: O(n) // n = len(s)