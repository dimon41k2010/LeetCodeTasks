class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        int_lst = set()
        i = 0
        while i < len(word):
            if word[i].isdigit():
                start = i
                while i < len(word) and word[i].isdigit():
                    i += 1
                int_lst.add(int(word[start:i]))
            # else: # smart improvements
            i += 1
        return (len(int_lst))

#Time: O(N)
#Space: O(N)