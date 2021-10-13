class Solution:
    def countSegments(self, s: str) -> int:
        
        counter = 0
        is_space = True

        for char in s:
            if char == ' ':
                is_space = True
            else:
                if is_space:
                    counter += 1
                    is_space = False

        return counter

# Time: O(n)
# Space: O(1)