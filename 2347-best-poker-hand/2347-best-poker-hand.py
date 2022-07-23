class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        
        suits_set = set(suits)
        if len(suits_set) == 1:
            return "Flush"

        dic = Counter(ranks)
        if any([val >= 3 for val in dic.values()]):
            return "Three of a Kind"

        if any([val >= 2 for val in dic.values()]):
            return "Pair"

        return "High Card"
    
    

#Time: O(1)
#Space: O(1)