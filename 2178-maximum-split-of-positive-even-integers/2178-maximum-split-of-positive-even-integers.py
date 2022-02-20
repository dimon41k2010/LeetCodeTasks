class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        if finalSum % 2 != 0:
            return []
        
        res = []
        level = 2
        while finalSum > 0:
            if finalSum - level <= level: 
                res.append(finalSum)
                finalSum = 0
            else:
                res.append(level)
                finalSum -= level
                level += 2
        return res