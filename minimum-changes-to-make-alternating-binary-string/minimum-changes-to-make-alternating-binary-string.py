class Solution:
    def minOperations(self, s: str) -> int:
        
#         def count_changes(s_list):
#             res = 0
#             print(s_list)
#             for i in range(1, len(s_list)):
#                 if s_list[i] == s_list[i-1]:
#                     s_list[i] = "1" if s_list[i] == "0" else "0"
#                     res += 1
#             return res

#         return(min(count_changes(list(s)), count_changes(list(s)[::-1])))
        
    
        count = 0
        count1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    count += 1
                if s[i] == '0':
                    count1 += 1
            else:
                if s[i] == '0':
                    count += 1
                if s[i] == '1':
                    count1 += 1
        return min(count, count1)