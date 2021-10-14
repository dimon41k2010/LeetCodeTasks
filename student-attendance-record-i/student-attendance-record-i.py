class Solution:
    def checkRecord(self, s: str) -> bool:
        counter_A = 0
        counter_L = 0

        for letter in s:
            if letter == "A":
                counter_A += 1
                counter_L = 0
            elif letter == "L":
                counter_L += 1
            else:
                counter_L = 0

            if counter_L >= 3 or counter_A >= 2:
                return(False)
        return True