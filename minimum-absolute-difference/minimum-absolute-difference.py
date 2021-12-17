class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        min_diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < min_diff:
                min_diff = diff
        # print(min_diff)

        res = []
        for i in range(1, len(arr)):
            pair = arr[i] - arr[i-1]
            if pair == min_diff:
                res.append([arr[i-1], arr[i]])
        return (res)

#Time: O(N Log N) + O(N)
#Space: O(1)