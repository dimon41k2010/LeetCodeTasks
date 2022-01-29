class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def is_palindrome(word):
            left = 0
            right = len(word)-1
            while left < right:
                if word[left] == word[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        for word in words:
            if is_palindrome(word):
                return word

        return ""


# Time: O(N * W) // W=len(word)
# Space: O(1) 