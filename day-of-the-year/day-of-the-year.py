class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split('-')                  #O(N)
        year, month, day = int(year), int(month), int(day)
        leap = 1 if year % 4 == 0 else 0
        d = {1: 31, 2:28 + leap, 3:31, 4:30, 5:31, 6:30, 7: 31, 8:31, 9:30, 10:31, 11:30, 12:31}

        res = 0
        for key in range(1,month):  #O(12)
            res += d[key]
        res += day
        return (res)

#Time: O(N) + O(12)
#Space: O(1)