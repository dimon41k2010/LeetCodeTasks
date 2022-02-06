class Solution:
    def minimumSum(self, num: int) -> int:
        
        num_arr = [ int(digit) for digit in str(num) if digit != "0" ]
        num_arr.sort()
        num_arr.reverse()
        res = 0
        for i in range(len(num_arr)):
            if i <= 1:
                res += num_arr[i]
            elif i > 1:
                res += num_arr[i] * 10
        return (res)

# Time: O(N) + O(N log N) // N=len(num)
# Space: O(N) // N=len(num)