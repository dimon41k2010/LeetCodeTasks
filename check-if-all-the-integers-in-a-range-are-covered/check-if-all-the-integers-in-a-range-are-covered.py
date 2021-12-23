class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:


        def get_start(range_):
            return range_[0]

        ranges.sort(key=get_start)
        index = 0
        for i in range(left, right+1):
            while i < ranges[index][0] or ranges[index][1] < i:
                index += 1
                if index >= len(ranges):
                    return (False)

        return (True)


#Time: O(N Log N) + O(N) => O(N)
#Space: O(1)