class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def get_letter_to_index(letter):
            return str(ord(letter) - ord('a'))

        def get_word_to_num(word):   #O(N)
            res = []
            for char in word:
                res.append(get_letter_to_index(char))
            return int(''.join(res))

        return (get_word_to_num(firstWord) + get_word_to_num(secondWord) == get_word_to_num(targetWord))

#Time: O(N1 + N2 + N3)
#Space: O(N1 + N2 + N3) 