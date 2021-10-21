class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(data):     # O(N)
            return data == data[::-1]

        return (1 if is_palindrome(s) else 2)

#Time: O(N)
#Space: O(N)
        
