class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_p = prices[0]
        profit = 0
        for i in range(1, len(prices)): # 2
            if prices[i] < min_p:  # 7<1 
                min_p = prices[i]
            else:
                int_temp = prices[i] - min_p
                if int_temp > profit:
                    profit = int_temp
        return profit
    
    
    #Time: O(n) + O(n)
    #Space: O(1)
    