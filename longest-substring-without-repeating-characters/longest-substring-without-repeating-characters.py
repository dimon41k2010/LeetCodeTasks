class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_sub_str = set()
        delete_inx = 0
        res = 0
        for char in s:
            if char in set_sub_str:

                while s[delete_inx] != char:
                    set_sub_str.remove(s[delete_inx])
                    delete_inx += 1

                delete_inx += 1
            else:
                set_sub_str.add(char)
            
            res = max(res, len(set_sub_str))
        
        return (res)
    
# Time: O(N * 2) = O(N)
# Space: O(N)