class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        for word in words:   # O(N * W)
            for char in word:
                if char in d.keys():
                    d[char] += 1
                else:
                    d[char] = 1
        # print(d)
        for key in d.keys():
            if d[key] % len(words) != 0:
                return (False)
        return True

#Time: O(N * W) + O(26) 
#Space: O(26)
        
        
    