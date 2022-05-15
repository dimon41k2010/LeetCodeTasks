class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
#         special.append(bottom - 1)
#         special.append(top + 1)
#         special.sort()

#         consecutive = -1
#         for i in range(1, len(special)):
#             consecutive = max(consecutive, special[i] - special[i-1] - 1)
#         return (consecutive)

#Time: O(N Log N) + O(N) => O(N Log N)
#Space: O(1)


# List comprehension
        special.append(bottom - 1)
        special.append(top + 1)
        special.sort()

        return (max([special[i] - special[i-1]- 1 for i in range(1, len(special))]))

#Time: O(N Log N) + O(N) => O(N Log N)
#Space: O(N)