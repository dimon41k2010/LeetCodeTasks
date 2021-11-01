class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and len(trust)==0:
            return (1)
        d = {}
        for val in trust:
            a, b = val
            if b not in d.keys():
                d[b] = 1
            else:
                d[b] += 1
        
        candidate = None
        for key in d.keys():
            if d[key] == n-1:
                candidate = key
        if candidate == None:
            return (-1)

        for val in trust:
            a, b = val
            if a == candidate:
                return (-1)
        return (candidate)
    
#Time: O(N)
#Space: O(N)