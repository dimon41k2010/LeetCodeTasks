class Solution:
    def countPoints(self, rings: str) -> int:
        
        rods = [ set() for _ in range(10) ]  # Time: O(1)

        for i in range(0, len(rings), 2):   # Time: O(N/2)
            rods[int(rings[i+1])].add(rings[i])

        return sum([ 1 for rod in rods if len(rod)==3  ])  #Time: O(1)


# Time: O(1) + O(N/2) + O(1) = O(N)
# Space: O(1) + O(1) = O(1)