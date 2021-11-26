class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # res = 0
        # while tickets[k] != 0:
        #     for i in range(len(tickets)):
        #         if tickets[i] > 0:
        #             tickets[i] -= 1
        #             res += 1
        #             # print(tickets)
        #         if tickets[k] == 0:
        #             break
        # return res

# Time: O(N * T) // T = max(tickets[i])
# Space: O(1)


        return (sum( [ min(tickets[i], tickets[k] if k >= i else tickets[k]-1) for i in range(len(tickets))] ))
# Time: O(N)
# Space: O(N)