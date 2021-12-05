class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five = 0
        count_ten = 0

        for bill in bills:
            if bill == 5:
                count_five += 1
            elif bill == 10 and count_five >= 1:
                count_ten += 1
                count_five -= 1
            elif bill == 20 and count_five >= 1 and count_ten >= 1:
                count_five -= 1
                count_ten -= 1
            elif bill == 20 and count_five >= 3:
                count_five -= 3
            else:
                return (False)
        return (True)
        
# Time: O(N)
# Space: O(1)