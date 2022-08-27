class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        res = sum(energy)+1 - initialEnergy

        if res < 0:
            res = 0
        for val in experience:
            if val >= initialExperience:
                res += (val + 1) - initialExperience
                initialExperience += (val + 1) - initialExperience
            initialExperience += val
        
        return (res)

#Time: O(N)
#Space: O(1)