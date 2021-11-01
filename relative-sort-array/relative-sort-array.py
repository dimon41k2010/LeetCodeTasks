class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        d={}
        for i in range(len(arr1)):        # O(N)
            if arr1[i] not in d.keys():
                d[arr1[i]] = 1
            else:
                d[arr1[i]] += 1
        res = []
        for i in range(len(arr2)):       # O(N)
            n = d[arr2[i]]
            for _ in range(n):
                res.append(arr2[i])
        arr2_set = set(arr2)
        # tail = []
        # for i in range(len(arr1)):       # O(N)
        #     if arr1[i] not in arr2_set:
        #         tail.append(arr1[i])
        # tail.sort()                    #O(N log N)
        # print(res + tail)
        
        count_array = [ 0 for i in range(1001)]
        for i in range(len(arr1)):
            if arr1[i] not in arr2_set:
                count_array[arr1[i]] += 1
        for i in range(len(count_array)):
            while count_array[i] > 0:
                res.append(i)
                count_array[i] -= 1
        return (res)