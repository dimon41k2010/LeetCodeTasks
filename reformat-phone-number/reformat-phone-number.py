class Solution:
    def reformatNumber(self, number: str) -> str:
        clean_number = []
        for digit in number:                 # O(N)
            if digit.isnumeric():
                clean_number.append(digit)
        clean_number = "".join(clean_number)  # O(N)
        i = 0
        res = []
        while i < len(clean_number):          # O(N/3)
            if len(clean_number) - i <= 4:
                if len(clean_number) - i <= 2:
                    res.append(clean_number[i:i+2])
                elif len(clean_number) - i <= 3:
                    res.append(clean_number[i:i+3])
                elif len(clean_number) - i <= 4:
                    res.append(clean_number[i:i+2] + "-" + clean_number[i+2:i+4])
                break
            else:
                res.append(clean_number[i:i+3] + "-")
                i += 3
        return (''.join(res))

#Time: O(N) + O(N) + O(N/3) = O(N)
#Space: O(N) + O(N) = O(N)