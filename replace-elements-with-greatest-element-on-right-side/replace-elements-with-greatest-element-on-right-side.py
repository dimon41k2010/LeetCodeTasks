class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        def solve_recur(index, arr):
            # print("Enter: ", index, arr)
            if index == len(arr):
                return -1
            curr_val = solve_recur(index + 1, arr)
            # print("Mid: ", index, arr, "| right_max", curr_val, "| arr[index]:", arr[index])

            res_max = arr[index]
            if curr_val > res_max:
                res_max = curr_val

            arr[index] = curr_val
            # print("Exit: ", index, arr, "| res_max", res_max)
            return res_max

        # print(arr)
        solve_recur(0, arr)
        # print(arr)
        
        return arr
    
    
    
#Time: O(N)
#Space: O(N)
        
        