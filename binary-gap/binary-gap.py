class Solution:
    def binaryGap(self, n: int) -> int:
        
        
        def remove_right_zeros(n):
            if (n % 2) == 1:
                return n
            elif (n % 2) == 0:
                return remove_right_zeros(n//2)

        def get_binary(n, count):
            # print("Enter:", count, "|",n % 2,"|", n, bin(n) )
            if n == 0:
                return 0

            if (n % 2) == 1:

                count = 0
            elif (n % 2) == 0:
                count += 1

            next_return = get_binary(n // 2, count)
            # print("exit:", count, "|",n % 2,"|", n, bin(n), next_return )

            return max(count, next_return)
        n = remove_right_zeros(n)
        
        if n == 1: 
            return 0
        
        return get_binary(n, 0) + 1
        


# Time: O(Log N)
# Space: O(Log N)