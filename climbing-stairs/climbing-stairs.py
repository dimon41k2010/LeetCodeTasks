class Solution:
    def climbStairs(self, n: int) -> int:
        
        distinct = [0,1,2]

        for i in range(3, n + 1):
            cur_val = distinct[i-1] + distinct[i-2]
            distinct.append(cur_val)
        return (distinct[n])

# Time: O(N)
# Space: O(N)
        