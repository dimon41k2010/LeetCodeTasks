class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        def convert_to_min(time):
            time_parts = time.split(":")
            return int(time_parts[0])*60 + int(time_parts[1])
        
        def is_intersection(event1, event2):
            return convert_to_min(event1[0]) <= convert_to_min(event2[0]) \
                   and convert_to_min(event2[0]) <= convert_to_min(event1[1])

        return (is_intersection(event1,event2) or is_intersection(event2, event1))

#Time: O(1)
#Space: O(1)