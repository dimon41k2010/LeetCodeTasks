class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost.sort() # Time: O(N lon N)
        count = 1
        total_sum = 0
        for i in range(len(cost)-1,-1,-1):
            if count % 3 != 0:
                total_sum += cost[i]
            count += 1

        return (total_sum)

# Time: O(N lon N) + O(N) = O(N lon N)
# Space: O(1)
        
    
        # cost.sort()      # Time: O(N lon N)
        # cost.reverse()   # Time: O(N)
        # return (sum([ val for i, val in enumerate(cost) if (i+1) % 3 != 0 ]))

# Time: O(N lon N) + O(N) + O(N) = O(N lon N)
# Space: O(N/3) = O(N)