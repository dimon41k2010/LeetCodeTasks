class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        def delete(s, inx):
            return s[:inx] + s[inx+1:]  # O(2*N)

        res = ''
        res_max = -1
        for i in range(len(number)):
            if number[i] == digit:
                candidate = delete(number, i)
                candidate_value = int(candidate)
                if candidate_value > res_max:
                    res_max = candidate_value
                    res = candidate

        return (res)
    
    
#Time: O(N*N)
#Space: O(N)