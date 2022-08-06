class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        
        def helper(s):
            i = 0
            res = []
            while i < len(s):
                count = 1
                while i+1 < len(s) and s[i] == s[i+1]:
                    i += 1
                    count += 1
                else:
                    i += 1
     
                res.append(str(count) + s[i-1])
            return "".join(res)

        for _ in range(n-1):
            res = helper(res)
        return (res)

#Time: O(2^N)
#Space: O(2^N)