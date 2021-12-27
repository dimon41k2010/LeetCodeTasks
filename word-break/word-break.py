class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         words_set = set(wordDict)
#         words_len_set = set([ len(word) for word in wordDict ])
#         words_len_set = reversed(sorted(list(words_len_set)))

#         def solve_recur(i, s):
#             if i == len(s):
#                 return True

#             for word_len in words_len_set:
#                 window = s[i : i+word_len]
#                 if window in words_set:
#                     if solve_recur(i+word_len, s):
#                         return True
#             return False

#         return solve_recur(0, s)


# Time: O(N ^ 26)  
# Space: O(N) // N=len(s)


        def recurse(start):
            
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            # find end indx
            for l in endIndexes:
                node = s[start: start+l]

                if node in dictSet and recurse(start+l):
                    memo[start+l] = True
                    return True
                
            memo[start] = False
            return False
            
        
        # main
        memo = {}
        start = 0
        
        endIndexes = []
        for w in wordDict:
            endIndexes.append(len(w))
        
        dictSet = set(wordDict)
        
        state = recurse(start)
        return state