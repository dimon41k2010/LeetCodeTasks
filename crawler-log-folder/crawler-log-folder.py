class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "./":
                continue
            if log == "../" and stack:
                stack.pop()
            elif log != "../":
                stack.append(log)
        return (len(stack))

#Time: O(N)
#Space: O(N)