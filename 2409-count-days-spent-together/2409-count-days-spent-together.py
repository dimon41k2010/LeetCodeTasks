class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def to_day_numbers(date_str):
            date_parts = date_str.split("-")
            res = int(date_parts[1])
            for i in range(0, int(date_parts[0])-1):
                res += months[i]
            return res

        days_together = min(to_day_numbers(leaveAlice),to_day_numbers(leaveBob)) - max(to_day_numbers(arriveAlice),to_day_numbers(arriveBob))
        
        return (days_together + 1 if days_together >= 0 else 0)

#Time: O(1)
#Space: O(1)