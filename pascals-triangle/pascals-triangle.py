class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]

        for i in range(1, numRows):
            temp_lst = [1]

            for j in range(1, len(res[-1])):
                prev_val = res[-1][j-1]
                cur_val = res[-1][j]
                temp_lst.append(sum([prev_val, cur_val]))

            temp_lst.append(1)
            res.append(temp_lst)

        return (res)

#Time: O(N^2)
#Space: O(N)