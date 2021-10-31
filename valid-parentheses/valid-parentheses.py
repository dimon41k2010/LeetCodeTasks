class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        stack = []                               # [ ]
        for val in s:
            if val not in d.keys():              # open parentheses
                stack.append(val)
            
            elif val in d.keys():                # closed parentheses
                if not stack or stack[-1] != d[val]: # empty stack OR top of stack not equal to current val
                    return False    
                else:                            # everything match
                    stack.pop()
            
        return True if not stack else False
    #Time: O(n) 
    #Space: O(n) + O(d)
    
        
#         stack = [s[0]]
#         for i in s[1:]:
#             if i == ']' and stack and stack[-1] == '[':
#                 stack.pop()
#             elif i == ')' and stack and stack[-1] == '(':
#                 stack.pop()
#             elif i == '}' and stack and stack[-1] == '{':
#                 stack.pop()
#             else:
#                 stack.append(i)
        
#         return True if not stack else False
    
    #Time: O(n) 
    #Space: O(n)