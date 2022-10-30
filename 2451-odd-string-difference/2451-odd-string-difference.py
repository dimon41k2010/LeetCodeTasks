class Solution:
    def oddString(self, words: List[str]) -> str:
        
        def incode(arr):
            return ",".join([str(num) for num in arr ])

        def get_inx(char):
            return ord(char)-ord("a")
        
        def get_diff(s):
            res = []
            for i in range(1, len(s)):
                res.append(get_inx(s[i]) - get_inx(s[i-1]))
            return res
        
        counter = Counter([incode(get_diff(word)) for word in words])

        for word in words:
            diff = get_diff(word)
            incoded = incode(diff)
            if counter[incoded] == 1:
                return(word)
        return (-1)

#Time: O(N)
#Space: O(1)