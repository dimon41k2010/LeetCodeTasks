class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []

        for i in range(len(prices)):
            is_found = False
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j] and is_found == False:
                    res.append(prices[i]-prices[j])
                    is_found = True
                    break
            if is_found == False:
                res.append(prices[i])

        return res

# Time: O(N^2)
# Space: O(1)