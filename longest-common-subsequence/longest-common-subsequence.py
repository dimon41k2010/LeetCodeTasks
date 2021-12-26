class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [ [0 for __ in text2 ] for _ in text1 ]
# print(dp)

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    prev_val = 0
                    if i-1 >= 0 and j-1 >= 0:
                        prev_val = dp[i-1][j-1]

                    dp[i][j] = prev_val+1
                elif text1[i] != text2[j]:
                    val_top = 0
                    if i-1 >= 0:
                        val_top = dp[i-1][j]
                    val_left = 0
                    if j-1 >= 0:
                        val_left = dp[i][j-1]

                    dp[i][j] = max(val_top, val_left)
        return(dp[-1][-1])
    
#Time: O(N^2)
#Space: O(N^2)
