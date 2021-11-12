class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = []
        d = {}  # O(1)
        m = len(score) 
        for i in range(m):
            d[score[i]] = i    #Space: O(n),  n=score
            res.append("")
        score.sort()     # O(N log N)
        for i in range(m-1,-1,-1):
            index_old = d[score[i]]
            if i == m-1:
                res[index_old] = "Gold Medal"
            elif i == m-2:
                res[index_old] = "Silver Medal"
            elif i == m-3:
                res[index_old] = "Bronze Medal"
            else:
                place = str(m - i)
                res[index_old] = place

        return res

#Time: O(n) + O(N log N) + O(n) = O(N log N)
#Space: O(n)