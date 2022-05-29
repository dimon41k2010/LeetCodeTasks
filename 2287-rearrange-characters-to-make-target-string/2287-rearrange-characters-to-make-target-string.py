class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        
        def count_dict(s):
            dict_s = {}
            for char in s:
                if char not in dict_s.keys():
                    dict_s[char] = 1
                else:
                    dict_s[char] += 1
            return dict_s

        count_s = count_dict(s)
        count_target = count_dict(target)
        res = len(s)
        for key in count_target.keys():
            if key in count_s.keys():
                res = min(res, count_s[key] // count_target[key])
            else:
                return 0
        return (res)
    
    
# list comprehension

#         def count_dict(s):
#             dict_s = {}
#             for char in s:
#                 if char not in dict_s.keys():
#                     dict_s[char] = 1
#                 else:
#                     dict_s[char] += 1
#             return dict_s

#         count_s = count_dict(s)
#         count_target = count_dict(target)
        
#         return min([0 if key not in count_s.keys() else count_s[key] // count_target[key] for key in count_target.keys()])

    
#Time: O(N)
#Space: O(N)


    