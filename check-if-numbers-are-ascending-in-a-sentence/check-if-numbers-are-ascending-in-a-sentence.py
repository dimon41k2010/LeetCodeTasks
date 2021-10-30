class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        i = 0
        prev = -1
        while i < len(s):
            if s[i].isdigit(): # O(1)
                start = i
                while i < len(s) and  s[i].isdigit():  # O(1)
                    i += 1
                num = int(s[start:i])
                if num <= prev:
                    return (False)
                prev = num
            else:
                i += 1
        return (True)

#Time: O(N)
#Space: O(1)