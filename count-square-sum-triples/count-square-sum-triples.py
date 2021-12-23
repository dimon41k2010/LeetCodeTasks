class Solution:
    def countTriples(self, n: int) -> int:
        set_ = set()

        for i in range(1, n+1):
            set_.add(i*i)

        res = 0
        for a2 in set_:
            for b2 in set_:
                if (a2 + b2) in set_:
                    res += 1
        return (res)

#Time: O(N) + (O(N) * O(N)) = O(N^2)
#Space: O(N)