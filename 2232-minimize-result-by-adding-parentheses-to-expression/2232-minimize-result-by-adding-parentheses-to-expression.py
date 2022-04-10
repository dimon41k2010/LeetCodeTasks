class Solution:
    def minimizeResult(self, expression: str) -> str:
        exp_parts = expression.split("+")
        num1 = exp_parts[0]
        num2 = exp_parts[1]
        
        min_val = int(num1) * int(num2)
        final_i1 = -1
        final_i2 = -1

        for i1 in range(0,len(num1)):
            for i2 in range(1, len(num2) + 1):
                num4 = 1
                if i1 != 0:
                    num4 = int(num1[:i1])

                num5 = int(num1[i1:])
                num6 = int(num2[:i2])

                num7 = 1
                if i2 != len(num2):
                    num7 = int(num2[i2:])

                value = num4 * (num5 + num6) * num7
                if value < min_val:
                    min_val = value
                    final_i1 = i1
                    final_i2 = i2

        if len(num1) == 1:
            final_i1 = 0
        if len(num2) == 1:
            final_i2 = 1
        
        return (num1[:final_i1] + '(' + num1[final_i1:] + "+" + num2[:final_i2] + ")" + num2[final_i2:])

# Time: O(N^2)
# Space: O(N)