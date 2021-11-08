class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        m = len(mat)
        n = len(mat[0])
        if m * n != r*c:
            return mat

        for i in range(m):  # r
            for k in range(n): # c
                temp.append(mat[i][k])

        ind = 0
        res = []
        for i in range(0,r):
            temp_l = []
            for k in range(0,c):
                temp_l.append(temp[ind])
                ind += 1
            res.append(temp_l)

        return res

# Time: O(n) * O(m) + O(r) * O(c) = O(r*c)
# Space: O(m*n) + O(c)
#===========


# To learn from discussions: 

#         if len(mat) * len(mat[0]) != r * c:
#             return mat

#         ans = [[]]
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 k = mat[i][j]
#                 if len(ans[-1]) < c:
#                     ans[-1].append(k)
#                 else:
#                     ans.append([k])
#         return ans