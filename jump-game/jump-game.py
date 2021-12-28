class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
# First solution, Greedy algo

        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


# Time: O(N)
# Space: O(1)
        
# ========       
# Ssecond solution, recursion, with Time Limit Excided error

        memo = set()

        def solve_recur(i):

            if i == len(nums)-1:
                return True

            if i in memo:
                return False

            for j in range(1, nums[i]+1):
                if solve_recur(i + j):
                    return True

            memo.add(i)
            return False

        return solve_recur(0)

# Time: O(N*M)
# Space: O(N)