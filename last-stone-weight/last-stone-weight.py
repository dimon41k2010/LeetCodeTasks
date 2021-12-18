class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        def des_comparator(e):
            return -e
        
        pri_queue = []
        for stone in stones:
            heapq.heappush(pri_queue, (des_comparator(stone), stone))
            
        while len(pri_queue) > 1:
            first = heapq.heappop(pri_queue)[1]
            second = heapq.heappop(pri_queue)[1]
            stone = first - second
            heapq.heappush(pri_queue, (des_comparator(stone), stone))
        
        return (heapq.heappop(pri_queue)[1])
    
#Time: O(log N) + O(N)
#Space: O(N)