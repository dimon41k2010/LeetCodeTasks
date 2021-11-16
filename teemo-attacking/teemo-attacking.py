class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # timeSeries = [1,2,7,8], duration = 2 
        # [0,1,2,3,4,5,6,7,6,8,9,10]
        #  total = [1,2,  2,3  7,8, 8,9] = 6
        
        res = 0
        last_poison = -1
        for i in range(len(timeSeries)):
            if i != 0 and last_poison >= timeSeries[i]:
                val = last_poison - timeSeries[i] + 1  
                res += -val         
            res += duration  
            last_poison = timeSeries[i] + duration -1  
        return res
    
    
# Time:  O(n)
# Space: O(1)