class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        def sorted(word):  # O(N)
            d = {}
            for char in word:
                if char not in d.keys():
                    d[char] = 1
                else:
                    d[char] += 1
            res = []
            for i in range(ord("a"), ord("z")+1):
                c = chr(i)
                if c in d.keys():
                    res.append(c * d[c])

            return ''.join(res)

        
        prev = None
        res = []
        for word in words:
            sorted_word = sorted(word)
            if sorted_word != prev:
                prev = sorted_word
                res.append(word)
        return (res)

#Time:  O(N * M) / N = len(words), M = len(word)
#Space: O(N * M) / N = len(words), M = len(word)