class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        counter = 0
        
        def is_token(word):
            for char in word:
                if char.isdigit():
                    return False
            if word[0] == "-" or word[-1] == "-":
                return False
            hyphen_count = word.count("-")
            if hyphen_count > 1:
                return False
            punct_count = len([letter for letter in word if letter in ['!', '.', ','] ])
            if punct_count > 1:
                return False
            if punct_count == 1 and word[-1].isalpha():
                return False
            if len(word) > 2 and word[-2] == "-" and punct_count == 1:
                return False
            
            return True
        
        return(len([word for word in words if is_token(word)]))

#Time: O(N) + O(N * W)  // N-> len(words), W->len(word)
#Space: O(N) + O(N * W) // N-> len(words), W->len(word)
        
    