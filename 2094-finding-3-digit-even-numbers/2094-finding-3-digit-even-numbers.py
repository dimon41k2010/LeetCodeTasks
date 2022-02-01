class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        count_d = {}    # Time: O(N)
        for digit in digits:
            if digit in count_d.keys():
                count_d[digit] += 1
            else:
                count_d[digit] = 1

        def is_valid(num, count_d):     # Time: O(1)
            while num > 0:
                digit = num % 10
                if digit in count_d.keys() and count_d[digit] > 0:
                    count_d[digit] -= 1
                else:
                    return False
                num //= 10
            return True

        res = []
        for num in range(100, 1000, 2):     # Time: O(1)
            if is_valid(num, count_d.copy()):
                res.append(num)
        return (res)

# Time: O(N) + O(1) + O(1)
# Space: O(1)