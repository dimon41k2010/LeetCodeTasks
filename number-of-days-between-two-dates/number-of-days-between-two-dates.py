class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        def is_leap(year):
            if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
                return True 
            return False
        
        def daySince1900(date):
            year, month, day = date.split('-')                  #O(N)
            year, month, day = int(year), int(month), int(day)
            leap = 1 if is_leap(year) else 0
             
            d = {1: 31, 2:28 + leap, 3:31, 4:30, 5:31, 6:30, 7: 31, 8:31, 9:30, 10:31, 11:30, 12:31}

            res = 0
            for key in range(1,month):  #O(12)
                res += d[key]
            res += day
            for y in range(1900, year):
                res += 365 + (1 if is_leap(y) else 0)
            return (res)
        
        return (abs(daySince1900(date2) - daySince1900(date1)))