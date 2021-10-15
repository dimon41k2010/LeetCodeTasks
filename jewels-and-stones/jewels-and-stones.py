class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        set_jewels = set(jewels)
        for stone in stones:   #O(n)
            if stone in set_jewels:  #O(1)
                res += 1
        return (res)

# Time: O(n + m) m=stones, (O(1) set(n)=jewels)
# Space: O(n)

# second option
#print( sum(stones.count(jewel) for jewel in jewels) )