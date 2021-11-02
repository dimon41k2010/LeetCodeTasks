# from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
       
        d = {}
        for card in deck:
            if card not in d.keys():
                d[card] = 1
            else:
                d[card] += 1

        min_count = len(deck)
        for val in d.values():
            if val < min_count:
                min_count = val

        for pos_candidate in range(2, min_count + 1):  #  O(C * Pr) -> O(N) / C->range(2, min_count + 1)
            is_success = True                                              # Pr -> len(d)
            for val in d.values():
                if val % pos_candidate == 0:
                    pass
                else:
                    is_success = False
            if is_success:
                 return True
        return False

# Time: O(C * Pr) -> O(N)
# Space: O(N)
# ====================

# With list comprehension
#         d = Counter(deck)

#         min_count = min(d.values())   # O(P) / P-> pairs

#         for pos_candidate in range(2, min_count + 1):
#             if all([val % pos_candidate == 0 for val in d.values()]):
#                 return True
#         return False

# Time: O(C * Pr) -> O(N)
# Space: O(N)