class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        order_dict = {num:i + 1  for i, num in enumerate(sorted(set(arr))) } # O(N log N) + O(N)
        return [ order_dict[num] for num in arr ]

# Time: O(N log N) + O(N) = O(N log N)
# Space: O(N) + O(N) + O(N) = O(N)