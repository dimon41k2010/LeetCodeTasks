class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}                          # d = {'h':0,
        for i in range(len(order)):   #      'l':1,
            d[order[i]] = i           #      'a':2}

        for i in range(1,len(words)):   #Time: O(N)
            if not is_bigger(words[i-1],words[i],d):
                return (False)
        return (True)

def is_bigger(word1, word2,d):
    for i in range( min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            return d[word1[i]] < d[word2[i]]
    return len(word1) <= len(word2)

# Time: O(26) + O(N) * O(W) = O(N^2)
# Space: O(26)