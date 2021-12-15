class Solution:
    def addDigits(self, num: int) -> int:
        
#         while num > 9:
#             temp_num = num
#             sum_num = 0
#             while temp_num != 0:
#                 sum_num += temp_num % 10
#                 temp_num  = temp_num // 10
#             num = sum_num

#         return (num)

#Time: O(Log N) -> O(1) * O(N) => O(N)
#Space: O(1)



# 2nd solution using recursion 
    
        def sum_recur(curr_num):
            if curr_num == 0:
                return 0

            other = sum_recur(curr_num//10)
            
            return (curr_num % 10) + other

        
        def solve_recur(accumul_num):
        
            if accumul_num <= 9:
                return accumul_num

            sum_num = sum_recur(accumul_num)
            next_return = solve_recur(sum_num)
            return next_return
        
        return(solve_recur(num))

#Time: O(Log N) -> O(1) * O(N) => O(N)
#Space: O(N)


