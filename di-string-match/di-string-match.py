class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        minim = 0
        maxim = len(s)

        for char in s:
            if char == "I":
                res.append(minim)
                minim += 1
            else:
                res.append(maxim)
                maxim -= 1
        res.append(minim)
        return res