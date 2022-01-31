class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        res = 0
        while maxDoubles > 0 and target != 1:
            if target % 2 != 0:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            res += 1

        return (res + target - 1)
    

# Time: O(log T) // T->target
# Space: O(1)