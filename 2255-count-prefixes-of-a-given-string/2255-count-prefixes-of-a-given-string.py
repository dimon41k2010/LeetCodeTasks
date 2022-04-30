class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        def is_prefix(pref):
            if len(pref) > len(s):
                return False
            for i in range(len(pref)):
                if pref[i] != s[i]:
                    return False
            return True


        return (sum([ 1 for word in words if is_prefix(word)]))


# Time: O(N*M) // N=len(words), M=len(word)
# Space: O(N)