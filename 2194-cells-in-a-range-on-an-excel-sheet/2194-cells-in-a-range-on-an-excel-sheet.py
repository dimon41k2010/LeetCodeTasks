class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        lower_leter_inx = ord(s[0])
        lower_numb = int(s[1])
        upper_leter_inx = ord(s[3])
        upper_numb = int(s[4])

        res = []
        for letter_inx in range(lower_leter_inx, upper_leter_inx + 1):
            for numb in range(lower_numb, upper_numb + 1):
                res.append(chr(letter_inx) + str(numb))
        return (res)

# Time: O(N * L) / L = 26, N = 9
# Space: O(1)