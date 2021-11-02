class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
#         d = {}

        def validate(domino_piece):         # O(1)
            if domino_piece[0] > domino_piece[1]:
                return [domino_piece[1], domino_piece[0]]
            return domino_piece

        def hash(domino_tile):               # O(1)
            return domino_tile.__str__()

#         for domino_tile in dominoes:
#             domino_tile = validate(domino_tile)
#             key = hash(domino_tile)
#             if key not in d.keys():
#                 d[key] = 1
#             else:
#                 d[key] += 1
#         res = 0
#         for val in d.values():              # O(N)
#             res += (val * val - val) // 2
#         return (res)

# Time: O(N)
# Space: O(1)
        
        
# Second solution
        # from collections import Counter

        d = Counter([ hash(validate(domino_tile)) for domino_tile in dominoes ]) #Space: O(N)
        result = sum([ (val * val - val) // 2 for val in d.values() ])      #Space: O(1)
        return (result)
    
# Time: O(N)
# Space: O(N)