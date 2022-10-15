class Solution:
    def countTime(self, time: str) -> int:
        
        [hours, minutes] = time.split(":")

        hour_combination = 1
        if hours[0] == "?" and hours[1] == "?":
            hour_combination = 24
        elif hours[0] == "?":
            hour_combination = 3 if int(hours[1]) < 4 else 2
        elif hours[1] == "?":
            hour_combination = 10 if int(hours[0]) < 2 else 4

        minutes_combination = 1
        if minutes[0] == "?" and minutes[1] == "?":
            minutes_combination = 60
        elif minutes[0] == "?":
            minutes_combination = 6
        elif minutes[1] == "?":
            minutes_combination = 10

        res = hour_combination * minutes_combination
        
        return (res)

#Time: O(1)
#Space: O(1)
