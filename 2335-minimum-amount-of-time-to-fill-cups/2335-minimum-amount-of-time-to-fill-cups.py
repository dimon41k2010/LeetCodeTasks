import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:

        q = []
        for digit in amount:
            if digit != 0:
                heapq.heappush(q, -digit)
        
        res = 0
        while len(q) > 1:
            value1 = heapq.heappop(q)
            value2 = heapq.heappop(q)
            value1 += 1
            value2 += 1

            if value1 != 0:
                heapq.heappush(q, value1)
            if value2 != 0:
                heapq.heappush(q, value2)
            res += 1
        if len(q) > 0:
            res += -heapq.heappop(q)

        return res

#Time: O(A1 + A2 + A3) => O(1)
#Space: O(N)