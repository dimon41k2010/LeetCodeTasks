class Solution:
    def reverseVowels(self, s: str) -> str:
        
#         vow = set('aeiouAEIOU')
#         s_list = list(s)
#         left = 0
#         right = len(s)-1

#         while left < right:
#             if s_list[left] in vow and s_list[right] in vow:
#                 s_list[left], s_list[right] = s_list[right], s_list[left]
#                 left += 1
#                 right -= 1
#             elif s_list[left] not in vow:
#                 left += 1
#             elif s_list[right] not in vow:
#                 right -= 1
#         s = ''.join(s_list)
        
#         return s

#Time: O(n/2) + O(1) + O(n) = O(s)
#Space: O(1)-set + O(n) = O(n) n=len(s)


# second, a bit different solution
        vow = set('aeiouAEIOU')
        s_list = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            while (left < len(s_list) and s_list[left] not in vow):
                left += 1
            while (right >= 0 and s_list[right] not in vow):
                right -= 1
            if (left >= right):
                break
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
            
        s = ''.join(s_list)
        
        return s