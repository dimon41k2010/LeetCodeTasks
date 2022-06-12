class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        prev_limit = 0
        res = 0
        for bracket in brackets:
            money = min(bracket[0] - prev_limit, income - prev_limit)
            res += money * bracket[1] / 100
            prev_limit += money
        return (res)

#Time: O(N)
#Space: O(1)
        