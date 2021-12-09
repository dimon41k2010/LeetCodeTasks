class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        start, min_gain = 0, 0
        for i in range(len(gain)):
            start = start - gain[i]
            min_gain = max(-start, min_gain)
            # print(-start)
        return(min_gain)