class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = [ [False for j in range(len(s)) ] for i in range(len(s))  ]

        step = 0
        for step in range(len(s)):
            for i in range(len(s)-step):
                j = i + step
                if j - i <= 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        
        return(sum([ row.count(True) for row in dp  ]))

        
    