class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def convert(letters):       #Time: O(N) / #Space: O(N)
            lst = []
            for letter in letters:
                lst.append(str(ord(letter) - ord("a") + 1))
            return ''.join(lst)

        def transform(digits):      #Time: O(N) / #Space: O(1)
            sum_ = 0
            for digit in digits:
                sum_ += int(digit)
            return str(sum_)

        
        res = convert(s)
        for _ in range(k):
            res = transform(res)
        return (int(res))

#Time: O(N * K) // N->len(s), K-> k
#Space: O(N) 