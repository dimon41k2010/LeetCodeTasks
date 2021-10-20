class Solution:
    def removeDuplicates(self, S: str) -> str:
		# initilaizing the stack with stating element
        stack = [S[0]]
        for i in range(1,len(S)):  #O(N)
        # if last inserted element is same the remove both else add them to stack
            if len(stack) > 0 and stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        return ''.join(stack) #O(N)

#Time: O(N) + O(N)
#Space: O(N)   / N=len(S)
      
        # temp_s = S
        # is_found = True
        # while is_found:
        #     is_found = False
        #     for i in range(1, len(temp_s)):
        #         prev = temp_s[i-1]
        #         if temp_s[i] == prev:
        #             temp_s = temp_s[0:i-1] + temp_s[i+1:]
        #             is_found = True
        #             break
        # return temp_s
    
#Time: O(n^2)
#Space: O(N)