class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for word in words:
            for letter in word:
                if i == len(s) or letter != s[i]:
                    return(False)
                i += 1
            if i == len(s):
                return (True)
                
#Time: O(N * W)  // N->len(words), W->len(word)
#Space: O(1)

#Solution 2:
    
    
#         if len(s) > len(''.join(words)):
#             return False
        
#         return (s == ''.join(words)[:len(s)])

#Time: O(N)  // N->len(words)
#Space: O(N)