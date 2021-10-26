class Solution:
    def maximumTime(self, time: str) -> str:
        res = list(time)
        if res[0] == "?":
            if res[1] != "?" and int(res[1]) >= 4:
                res[0] = "1"
            else: 
                res[0] = "2"
        if res[1] == "?":
            if res[0] == "2":
                res[1] = "3"
            else:
                res[1] = "9"
        if res[3] == "?":
            res[3] = "5"
        if res[4] == "?":
            res[4] = "9"

        return ("".join(res))

#Time: O(1)
#Space: O(N) // N-len(time) = 5