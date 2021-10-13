class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        longest_num = max(len(num1), len(num2))

        index1 = len(num1)-1
        index2 = len(num2)-1

        for i in range(longest_num):
            sum = carry
            carry = 0
            if index1 >= 0:
                sum += int(num1[index1])
            if index2 >= 0:
                sum += int(num2[index2])
            if sum >= 10:
                carry = 1
                sum = sum % 10
            index1 -= 1
            index2 -= 1
            res.append(str(sum))

        if carry == 1:
            res.append(str(carry))

        return ("".join(res[::-1]))
    
# Time: O(n) + O(1) + O(n) = O(n) (n=len(longest_num))
# Space: O(n)  (n=len(longest_num))