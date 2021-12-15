class Solution:
    def longestPalindrome(self, s: str) -> str:
     
    
        n = len(s) 
        dp = [[False] * n  for _ in range(n)]
        
        ans = ''
        for i in range(n):
            dp[i][i] = True
            ans = s[i]            
        maxLen = 1
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):             
                if s[start] == s[end]:
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end+ 1]
    
        return ans
        

        # 2nd: Original solution. Leetcode has TLE with this solution.     
        
        dp = [ [False for j in range(len(s)) ] for i in range(len(s))]  #Time: O(N^2)
        # print(dp)

        step = 0
        res = 1
        str_res = s[0]
        r, c = 0, 0
        for step in range(len(s)):              # Time: O(N^2)
            for i in range(len(s)-step):
                j = i + step
                # print(i, j)
                if j - i <= 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j]:
                    l = ((j - i) + 1)
                    if l > res:
                        res = l
                        r = i
                        c = j
        return (s[r:c+1])

                
#Time: O(N^2) + O(N^2) + O(N^2) = O(N^2)
#Space: O(N^2)