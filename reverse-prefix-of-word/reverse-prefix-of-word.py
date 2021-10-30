class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        ch_inx = word.index(ch)
        res = []
        res.append(word[ch_inx::-1])
        res.append(word[ch_inx+1:])
        return ("".join(res))

#Time: O(N)
#Space: O(N)

#Second solution 

        # return("".join( [word[ch_inx::-1], word[ch_inx+1:]] ))

#Time: O(N)
#Space: O(N)