class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        def is_prefix(word, pref):
            if len(word) < len(pref):
                return False
            for i in range(len(pref)):
                if word[i] != pref[i]:
                    return False
            return True

        return(len([ 1 for word in words if is_prefix(word,pref)]))

#Time: O(N * M) // N=len(word), M=len(pref)
#Space: O(N) // N=len(word)