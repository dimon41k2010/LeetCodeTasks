class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in d.keys():
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        return (d.values())

    
#Time: O(N) * O(W log W) // N->len(strs), W->len(s)
#Space: O(N * W)

# 2nd solution with custom sorting
        from collections import Counter

        d = {}
        def custom_sort(s):             # Time: O(W)
            d_sort = Counter(s)
            # print(d_sort)
            res = []
            for i in range(ord("a"), ord("z")+1):
                c = chr(i)
                count = d_sort[c] if c in d_sort.keys() else 0
                for _ in range(count):
                    res.append(c)
            return "".join(res)

        # print(custom_sort("eat"))

        for s in strs:
            sorted_s = custom_sort(s)   # Time: O(W)
            if sorted_s not in d.keys():
                d[sorted_s] = [s]
            else:
                d[sorted_s].append(s)
        return (d.values())

#Time: O(N) * O(W)
#Space: O(N * W)