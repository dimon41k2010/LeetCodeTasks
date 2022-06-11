class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()

        def count_pairs(potions, multiplier, condition):
            left = 0
            right = len(potions)-1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] * multiplier < condition:
                    left = mid + 1
                else:
                    right = mid - 1

            return len(potions)-right-1

        return([count_pairs(potions, spell, success) for spell in spells])

    
#Time: O(M log M) + O(N) * O(log M) => O(N Log N) // N = len(spells) M = len(potions)
#Space: O(1)