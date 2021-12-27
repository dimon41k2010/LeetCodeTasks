class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words_set = set(wordDict)
        words_len_set = set([ len(word) for word in wordDict ])
        memo = {}

        def solve_recur(i, s):
            # print("Enter", i)
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for word_len in words_len_set:
                window = s[i : i+word_len]
                if window in words_set:
                    if solve_recur(i+word_len, s):
                        return True
            
            memo[i] = False
            
            return False

        return solve_recur(0, s)


# Time: O(N ^ 26)  
# Space: O(N) // N=len(s)
