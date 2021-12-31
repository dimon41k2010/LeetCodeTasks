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

# Time: O(N ^ N)
# Space: O(T) + O(S) // T=target, S=set()
