class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # res = 0
        # for operation in operations:
        #     if operation[1] == "+":
        #         res += 1
        #     else:
        #         res -= 1
        # return (res)

#Time: O(N)
#Space: O(1)

#Second Solution
        return (sum([1 if i[1] == "+" else -1 for i in operations]))

#Time: O(N)
#Space: O(N)