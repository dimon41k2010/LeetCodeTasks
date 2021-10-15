class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        d={}
        for char in licensePlate:        # Time: O(n)
            if char.isalpha():
                char = char.lower()
                if char in d.keys():
                    d[char] += 1
                else:
                    d[char] = 1
        res = None
        for word in words:
            d_copy = d.copy()
            for letter in word:
                if letter in d_copy.keys():
                    d_copy[letter] -= 1
            is_letter_in_str = True

            for val in d_copy.values():
                if val > 0:
                    is_letter_in_str = False
            if is_letter_in_str and ( res == None or len(res) > len(word)):
                res = word
        return (res)

# Time: O(n) + O((N * W) + (N * L)) = O(n2)  // L=O(26) unique letters
# Space: O(26) = O(1)