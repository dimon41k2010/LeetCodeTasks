class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda l: l[0])

        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output
    
    #Time: sort-> O(N log n) + O(n)
    #Space: sort-> O(n) / O(1) ?
    
    
        # for start, end in intervals[1:]:
        #     lastEnd = output[-1][1]
        #     if start <= lastEnd:
        #         output[-1][1] = max(lastEnd, end)
        #     else:
        #         output.append([start, end])
        # return output