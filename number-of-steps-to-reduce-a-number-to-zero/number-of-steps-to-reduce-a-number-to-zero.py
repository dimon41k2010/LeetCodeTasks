class Solution:
    def numberOfSteps(self, num: int) -> int:

        # i=0
        # while num != 0:
        #     if num % 2 == 0:
        #         num = num / 2
        #     else:
        #         num -= 1
        #     i += 1
        # return(i)

#Time: O(2 Log N) => O(Log N)
#Space: O(1)

# Recursion solution
        def reduce_numb(num):
            # print("Enter", num)

            if num == 0:
                return 0
            temp = num
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1

            next_return = reduce_numb(num)
            # print("exit", temp, next_return)
            return 1 + next_return

        return reduce_numb(num)

#Time: O(2 Log N) => O(Log N)
#Space: O(2 Log N) => O(Log N)