class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def digits_sum(num): # 12
            res = 0
            while num > 0:
                res += num % 10 # 1
                num = num // 10 # 1
            return res

        d = {}
        for num in range(1, n+1): #1+9, 2+0
            key = digits_sum(num)
            if key in d.keys():
                d[key] += 1
            else:
                d[key] = 1


        max_count = 0
        for val in d.values():
            if val > max_count:
                max_count = val


        return (Counter( d.values())[max_count])