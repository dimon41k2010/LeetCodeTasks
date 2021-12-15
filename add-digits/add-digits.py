class Solution:
    def addDigits(self, num: int) -> int:
        
        while num > 9:
            temp_num = num
            sum_num = 0
            while temp_num != 0:
                sum_num += temp_num % 10
                temp_num  = temp_num // 10
            num = sum_num

        return (num)
    
    