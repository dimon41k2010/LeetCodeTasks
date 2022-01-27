class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        def short_word(word):
            return word.lower()  # Time: O(N)

        def capitalize(word):
            return word[0].upper() + word[1:].lower()  # Time: O(2*W)
        
        return ( ' '.join([ short_word(word) if len(word)<=2 else capitalize(word) for word in title.split(" ") ]) )

# Time: O(N) + O(N) // N = len(title)
# Space: O(N)