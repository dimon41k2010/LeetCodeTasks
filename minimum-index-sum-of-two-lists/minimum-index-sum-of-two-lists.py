class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        n = len(list1)
        m = len(list2)

        for i in range(n):
            d[list1[i]] = i

        least_sum = n + m
        res = []
        for i in range(m):
            if list2[i] in d.keys():
                temp_sum = d[list2[i]] + i
                if least_sum > temp_sum:
                    least_sum = temp_sum
                    res = []
                if least_sum == temp_sum:
                    res.append(list2[i])

        return res
    
    
# Time: O(n) + O(m)
#     len(list1) = n / len(list2) = m
#Space: O(n) n = len(list1)