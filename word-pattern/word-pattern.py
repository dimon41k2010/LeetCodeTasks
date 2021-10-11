class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n_s = s.split(' ')
        d = { }

        if len(pattern) != len(n_s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in d.keys():
                if n_s[i] in d.values():
                    return False

                d[pattern[i]] = n_s[i]

            else:
                if n_s[i] != d[pattern[i]]:
                    return False
        
        return True