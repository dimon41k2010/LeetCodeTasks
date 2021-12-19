class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0:
            return [0] 
        
        dp = [ -1 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1

        def counting_bits_recur(n, dp):
            # print("Enter", n , dp )
            if dp[n] != -1:
                return dp[n]
            dp[n] = n % 2 + counting_bits_recur(n // 2, dp)
            # print("Exit", n , dp )
            return dp[n]
        # counting_bits_recur(n, dp)

        # print(dp)

        for i in range(n+1):
            counting_bits_recur(i, dp)
        return(dp)

#Time: O(N) + O(N) + O(N) => O(N)
#Space: O(1)