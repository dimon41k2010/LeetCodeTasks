class Solution:
    def reformatDate(self, date: str) -> str:
        
        months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        day, month, year = date.split()
        res = [year, "-"]
        upd_month = months.index(month)
        if upd_month+1 < 10:
            res.append("0")
        res.append(str(upd_month+1))
        res.append("-")

        upd_day = int(day[:-2])

        if upd_day < 10:
            res.append("0")
        res.append(str(upd_day))

        return ''.join(res)

#Time: O(1)
#Space: O(1)