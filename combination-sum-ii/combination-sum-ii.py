class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if sum(candidates) < target:
            return ([])
        
        res = []
        lst = []
        set_ = set()
        candidates.sort()  #time O(N log N)

        def recur_sum(index, cur_sum):

            if cur_sum == target:
                lst_str = str(lst)
                if lst_str not in set_:
                    set_.add(lst_str)
                    res.append(lst.copy())
                return

            if index == len(candidates):
                return

            if cur_sum > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                lst.append(candidates[i])
                recur_sum(i+1, cur_sum + candidates[i])
                lst.pop()

        recur_sum(0, 0)
        return (res)

# Time: O(2 ^ N)
# Space: O(T) + O(S) // T=target, S=set()


# Second solution when we subtract from target
        candidates.sort()
        res = []
        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i+1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return (res)

# Time: O(2 ^ N)
# Space: O(T) + O(S) // T=target, S=set()