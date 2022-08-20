class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        def add_t0_dict(d, key):
            if key not in d.keys():
                d[key] = 1
            else:
                d[key] += 1

        def remove_from_dict(d, key):
            if d[key] == 1:
                d.pop(key)
            elif key in d:
                d[key] -= 1

        def max_value(d):
            return max(d.keys())

        res = []
        sub_len = 3
        for r in range(len(grid)-sub_len + 1):
            dict_storage = {}
            for sub_r in range(r, r + sub_len):
                for sub_c in range(0, sub_len):
                    add_t0_dict(dict_storage, grid[sub_r][sub_c])
            sub_res = [max_value(dict_storage)]
            for c in range(sub_len, len(grid)):
                prev_c = c - sub_len
                for sub_r in range(r, r + sub_len):
                    remove_from_dict(dict_storage, grid[sub_r][prev_c])
                    add_t0_dict(dict_storage, grid[sub_r][c])
                sub_res.append(max_value(dict_storage))
            res.append(sub_res)
        return (res)

#Time: O(N * M)
#Space: O(1)