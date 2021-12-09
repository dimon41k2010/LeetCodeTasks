class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        start, min_gain = 0, 0
        for i in range(len(gain)):
            start = start - gain[i]
            min_gain = max(-start, min_gain)
            # print(-start)
        return(min_gain)
    
#Time: O(N)
#Space: O(1)

# Second solution using list
        res_lst = [0]
        for i in range(len(gain)):
            res_lst.append(res_lst[-1] + gain[i])
        return(max(res_lst))

#Time: O(N)
#Space: O(N) / N -> len(res_lst)