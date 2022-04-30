class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        d = {"rows": {}, "cols": {} }
        
        def add(d, line_name, line_ind, is_guard, pos):
            if line_ind in d[line_name].keys():
                d[line_name][line_ind].append({"is_guard": is_guard, "pos": pos})
            else:
                d[line_name][line_ind] = [{"is_guard": is_guard, "pos": pos}]

        matrix = [ [ 0 for col in range(n)] for row in range(m)  ]

        for guard in guards:
            [r,c] = guard
            matrix[r][c] = 3

        for wall in walls:
            [r,c] = wall
            matrix[r][c] = 2

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 3:
                    add(d, "rows", row, True, col)
                    add(d, "cols", col, True, row)
                elif matrix[row][col] == 2:
                    add(d, "rows", row, False, col)
                    add(d, "cols", col, False, row)

        def is_valid(pos, line):
            if not line:
                return True

            left, right = 0, len(line)-1

            while left <= right:
                mid = (left + right) // 2
                if line[mid]["pos"] < pos:
                    left = mid + 1
                else:
                    right = mid -1
            # print(left, right)
            if right >= 0 and left < len(line):
                if line[left]["is_guard"] or line[right]["is_guard"]:
                    return False
            elif right < 0:
                if line[left]["is_guard"]:
                    return False
            elif left == len(line):
                if line[right]["is_guard"]:
                    return False

            return True


        res = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    is_row, is_col = False, False
                    if col in d["cols"] and is_valid(row, d["cols"][col]):
                        is_row = True
                    elif col not in d["cols"]:
                        is_row = True
                    if row in d["rows"] and is_valid(col, d["rows"][row]):
                        is_col = True
                    elif row not in d["rows"]:
                        is_col = True

                    if is_row and is_col:
                        res += 1
        return res

    
# Time: O(N*M)
# Space: O(N*M)