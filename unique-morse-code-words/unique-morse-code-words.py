class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
         ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
         ".--","-..-","-.--","--.."]

        s = set()
        for word in words:
            morse_word = []
            for letter in word:
                ind_morse = ord(letter) - ord("a")
                morse_word.append(morse[ind_morse])
            s.add(''.join(morse_word))

        return(len(s))

# Time: O(N) * O(W) + O(W*5) = O(n2)  // N=len(word)
# Space: O(N * W)