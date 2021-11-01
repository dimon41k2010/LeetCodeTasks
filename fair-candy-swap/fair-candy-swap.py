class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)                 # O(N)
        average = (alice_sum + sum(bobSizes)) // 2  # O(N)
        bobSizes_set = set(bobSizes)

        for val in aliceSizes:         # O(N)
            bobSize = average - (alice_sum - val)
            if bobSize in bobSizes_set:    # O(1)
                return (val, bobSize)

#Time: O(N)
#Space: O(N)