class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        # heights_sorted = sorted(heights)
        # res = 0
        # for i in range(len(heights)):
        #     if heights[i] != heights_sorted[i]:
        #         res += 1
        # return(res)

#Time: O(N Log N)
#Space: O(N)

# recursion solution

        heights_sorted = sorted(heights)

        def solve_recur(i, heights, heights_sorted): ##Time: O(N)

            if i == len(heights):
                return 0

            res = solve_recur(i+1, heights, heights_sorted)
            if heights[i] != heights_sorted[i]:
                res += 1

            return res

        return (solve_recur(0, heights, heights_sorted))

#Time: O(N Log N) + O(N) = O(N Log N)
#Space: O(N) + O(N)