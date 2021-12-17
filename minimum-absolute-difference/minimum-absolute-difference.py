class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
#         arr.sort()
#         min_diff = arr[1] - arr[0]
#         for i in range(1, len(arr)):
#             diff = arr[i] - arr[i-1]
#             if diff < min_diff:
#                 min_diff = diff
#         # print(min_diff)

#         res = []
#         for i in range(1, len(arr)):
#             pair = arr[i] - arr[i-1]
#             if pair == min_diff:
#                 res.append([arr[i-1], arr[i]])
#         return (res)

#Time: O(N Log N) + O(N)
#Space: O(1)

        arr.sort()
        
        def find_min_diff(index, arr):
            diff = arr[index] - arr[index-1]
            # print("Enter:", arr[index-1], arr[index], "{", diff,"}", arr )

            if index == len(arr)-1:
                return diff
            next_min_diff = find_min_diff(index + 1, arr)

            # print("Exit:", arr[index-1], arr[index], "{", diff, "} next_min_diff", next_min_diff, arr)
            return min(diff, next_min_diff)


        def get_all_pairs(min_diff, index, arr, res):
            if index == len(arr):
                return

            diff = arr[index] - arr[index-1]
            if diff == min_diff:
                res.append([arr[index-1], arr[index]])
            get_all_pairs(min_diff, index + 1, arr, res)


        min_diff = find_min_diff(1, arr)

        res = []
        get_all_pairs(min_diff, 1, arr, res)
        return (res)

    
#Time: O(N Log N) + O(N) + O(N)
#Space: O(N)