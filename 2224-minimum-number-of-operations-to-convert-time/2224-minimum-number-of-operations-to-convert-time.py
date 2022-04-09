class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        time_increase = [60, 15, 5, 1]
        
        def convert(time_line):
            time_parts = time_line.split(":")
            return int(time_parts[0]) * 60 + int(time_parts[1])

        lower = convert(current)
        upper = convert(correct)
        inx = 0
        res = 0
        while lower < upper and inx < len(time_increase):
            if lower + time_increase[inx] <= upper:
                lower += time_increase[inx]
                res += 1
            else:
                inx += 1

        return res

# Time: O(1)
# Space: O(1)