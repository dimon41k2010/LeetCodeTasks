class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        counter = 0
        len_word = len(searchWord)
        for word in sentence.split(): 
            if len(word) >= len_word and searchWord == word[0:len_word]:
                return(counter + 1)

            counter += 1
        return(-1)

#Time: O(C) + O(N)*O(W)  / C=len(sentence)  N=len(word.count)  W=len(word)
#Space: O(10) + O(C)