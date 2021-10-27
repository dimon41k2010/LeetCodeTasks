class Solution:
    def secondHighest(self, s: str) -> int:
        max_digit = -1
        second_max = -1
        for char in s:
            if char.isnumeric():
                num = int(char)
                if num == max_digit or num == second_max:
                    continue
                if max_digit < num:
                    second_max = max_digit
                    max_digit = num
                elif second_max < num:
                    second_max = num
        return (second_max)

#Time: O(N)
#Space: O(1)