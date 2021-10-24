class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        def check_chars(a,b):
            if a != b and a.lower() == b.lower():
                return True
            return False

        for char in s:
            if stack and check_chars(char,stack[-1]):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

#Time: O(N) 
#Space: O(N)