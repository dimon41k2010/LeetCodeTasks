class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        
        dic = {}

        for i in range(len(logs)):
            key = logs[i][0]
            value = logs[i][1] - (logs[i-1][1] if i > 0 else 0)
            if key not in dic.keys():
                dic[key] = value
            else:
                dic[key] = max(value, dic[key])

        res = -1
        max_value = -1
        for key in range(0, n+1):
            if key in dic.keys() and dic[key] > max_value:
                max_value = dic[key]
                res = key
        return (res)

#Time: O(L + N) // L=logs, N=n 
#Space: O(N)