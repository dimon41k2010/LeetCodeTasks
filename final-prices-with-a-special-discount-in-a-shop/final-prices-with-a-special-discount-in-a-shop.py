class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
#         res = []

#         for i in range(len(prices)):
#             is_found = False
#             for j in range(i+1, len(prices)):
#                 if prices[i] >= prices[j] and is_found == False:
#                     res.append(prices[i]-prices[j])
#                     is_found = True
#                     break
#             if is_found == False:
#                 res.append(prices[i])

#         return res

# Time: O(N^2)
# Space: O(1)

# ================
## Second APPROACH : STACK ##
## 1. Use Monotonic Increasing Stack Concept
## 2. Main idea is to find the Next Smaller Element in O(N) using #1
        stack = []
        for i, num in enumerate(prices):
            while(stack and prices[stack[-1]] >= num):
                popIndex = stack.pop()
                prices[popIndex] -= num
            stack.append(i)
        return (prices)

# Time: O(N)
# Space: O(1)