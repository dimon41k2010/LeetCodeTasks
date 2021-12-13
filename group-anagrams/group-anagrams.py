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