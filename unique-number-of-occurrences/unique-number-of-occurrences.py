class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
       
    # from collections import Counter
        
        d = Counter(arr)    # O(N)
        return (len(set(d.values())) == len(d.values()))  # O(N) -> set(d.values())

# Time: O(N)
# Space: O(N)