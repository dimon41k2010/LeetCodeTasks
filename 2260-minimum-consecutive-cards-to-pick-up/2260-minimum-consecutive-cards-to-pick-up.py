class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        res = len(cards)+1
        d = {}

        for i in range(len(cards)):
            if cards[i] in d.keys():
                res = min(i - d[cards[i]] + 1, res)
            d[cards[i]] = i

        if res == len(cards)+1:
            return -1
        
        return res


#Time: O(N)
#Space: O(N)
    