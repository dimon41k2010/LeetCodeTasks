class Solution:
    def largestInteger(self, num: int) -> int:
        
        count_dict = {}
        digits = []
        while num != 0:      #Time: O(N)
            digit = num % 10
            if digit not in count_dict.keys():
                count_dict[digit] = 1
            elif digit in count_dict.keys():
                count_dict[digit] += 1
            digits.append(digit)
            num //= 10

        digits.reverse()    #Time: O(N)
        odd_list = []
        even_list = []

        def add_to_list(digit, count_dict, lst):   #Time: O(N)
            if digit in count_dict.keys():
                for _ in range(count_dict[digit]):
                    lst.append(digit)

        for digit in range(0,10):  # Time: O(1)
            if digit % 2 == 0:
                add_to_list(digit, count_dict, even_list)  #Time: O(N)
            else:
                add_to_list(digit, count_dict, odd_list)   #Time: O(N)

        res_num = 0
        for digit in digits:  # Time: O(N)
            if digit % 2 == 0:
                res_num = res_num * 10 + even_list.pop()
            else:
                res_num = res_num * 10 + odd_list.pop()
        
        return (res_num)

# Time: O(N)
# Space: O(N)