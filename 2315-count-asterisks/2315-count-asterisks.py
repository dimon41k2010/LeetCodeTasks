class Solution:
    def countAsterisks(self, s: str) -> int:
        pair = 0
        n_s = s.split("|")
        # print(n_s)
        count = 0
        for i in range(0, len(n_s), 2):
            count += n_s[i].count("*")
        return (count)