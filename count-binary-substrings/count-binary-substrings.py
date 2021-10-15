class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zero = 0
        one = 0
        res = 0 
        is_zero = True
        for digits in s:
            if digits == "0" and is_zero:
                zero += 1
            elif digits == "1" and not is_zero:
                one += 1
            else:
                res += min(zero, one)
                if is_zero:
                    one = 1
                else:
                    zero = 1
                is_zero = not is_zero

        res += min(zero, one)
        return res

# Time: O(n)
# Space: O(1)
