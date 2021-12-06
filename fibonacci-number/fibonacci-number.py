class Solution:
    def fib(self, n: int) -> int:
        F = [0, 1]

        for i in range(2, n+1):
            F.append(F[i-1] + F[i-2])
        return (F[n])

# Time: O(N)
# Space: O(N)