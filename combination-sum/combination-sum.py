class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        lst = []
        res = []

        def solve_recur(index, sum_):

            if sum_ > target:
                return
            if sum_ == target:
                res.append(lst.copy())
                return

            for i in range(index, len(candidates)):
                lst.append(candidates[i])
                solve_recur(i, sum_ + candidates[i])
                lst.pop()

        solve_recur(0, 0)
        return res

# Time: O(N ^ N)
# Space: O(T) // T = target