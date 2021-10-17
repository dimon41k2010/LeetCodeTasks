class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        if backspace_deletion(s) == backspace_deletion(t):
            return (True)
        else: return (False)

def backspace_deletion(s):
    res_stack = []
    for char in s:
        if char == "#":
            if len(res_stack) > 0:
                res_stack.pop()
        else:
            res_stack.append(char)
    return ''.join(res_stack)