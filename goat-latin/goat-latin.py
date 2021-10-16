class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]
        words = sentence.split(' ')       # O(N)
        res_list=[]
        for i,word in enumerate(words):   # O(L)*O(W) = O(N)
            new_word = []
            if word[0] in vowels:
                new_word.append(word)
                new_word.append('ma')
            else:
                new_word.append(word[1:])
                new_word.append(word[0])
                new_word.append('ma')
            new_word.append('a'*(i+1))
            res_list.append(''.join(new_word))    # O(W)
            if i < len(words)-1:
                res_list.append(' ')

        return ''.join(res_list)                  # O(N)

# Time: O(N) +  O(L) * O(3W) = O(N)  // N=len(word)
# Space: O(N)