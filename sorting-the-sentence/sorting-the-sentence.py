class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        res = [ "" for i in range(len(lst))]    # O(N)
        for i in range(len(lst)):
            order = int(lst[i][-1])
            res[order-1] = lst[i][:-1]

        return (" ".join(res)) #O(N)

#Time: O(N) + O(N) + O(N) = O(N)
#Space: O(N) + O(N) = O(N)