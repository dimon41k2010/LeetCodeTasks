class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        def add_to_dict(d, key):
            if key not in d.keys():
                d[key] = 1
            else:
                d[key] += 1

        def remove_from_dict(d, key):
            if d[key] == 1:
                d.pop(key)
            elif key in d:
                d[key] -= 1

        def get_white(d, key = "W"):
            if key not in d.keys():
                return 0
            return d[key]

        d = {}
        for i in range(k):
            add_to_dict(d, blocks[i])
        res = get_white(d)
        for i in range(k, len(blocks)):
            prev_i = i - k
            remove_from_dict(d, blocks[prev_i])
            add_to_dict(d, blocks[i])
            res = min(get_white(d), res)
        return (res)

#Time: O(N)
#Space: O(1)