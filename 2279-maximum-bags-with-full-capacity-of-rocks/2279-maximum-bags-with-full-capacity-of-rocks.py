class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        diff = [capacity[i]-rocks[i] for i in range(len(rocks)) ]
        diff.sort()
        res = 0
        for val_diff in diff:
            if val_diff <= additionalRocks:
                additionalRocks -= val_diff
                res += 1
            else:
                return res

        return (res)

#Time: O(N Log N)
#Space: O(N)