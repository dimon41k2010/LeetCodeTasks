class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return "a" * n
        else: 
            return "a"+("b"*(n-1))