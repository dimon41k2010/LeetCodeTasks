class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        r,c=0,0
        R = len(mat)
        C = len(mat[0])
        first_logic = [[1, 0], [0,1]]
        second_logic = [[2,-1], [-1, 2]]
        logic_index = 0
        next_step = [[-1, 1], [1,-1]]
        next_step_index = 0
        result = []

        while r < R and c < C:
            result.append(mat[r][c])

            n_r = r + next_step[next_step_index][0]
            n_c = c + next_step[next_step_index][1]

            if n_r == R or n_c == C:
                n_r += second_logic[logic_index][0]
                n_c += second_logic[logic_index][1]
                logic_index = (logic_index + 1) % 2
                next_step_index = (next_step_index + 1) % 2
            elif n_r == -1 or n_c == -1:
                n_r += first_logic[logic_index][0]  
                n_c += first_logic[logic_index][1]      
                logic_index = (logic_index + 1) % 2
                next_step_index = (next_step_index + 1) % 2

            r = n_r
            c = n_c
            
        return result
    
# Time: O(N) ?
# Space: O(N) ?