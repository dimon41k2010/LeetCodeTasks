class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def sum_digit(num):  # O(N)
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        groups = {}
        for num in nums:  # O(N)
            key = sum_digit(num)
            if key not in groups.keys():
                groups[key] = [num]
            else:
                curr_list = groups[key]
                if len(curr_list) == 2:
                    min_value = min(curr_list)
                    if num > min_value:
                        curr_list.remove(min_value) # O(2)
                        curr_list.append(num)
                else:
                    curr_list.append(num)
                groups[key] = curr_list

        res = [sum(list(pair)) for pair in groups.values() if len(pair) == 2 ]
        
        return -1 if len(res) == 0 else max(res)  

#Time: O(N)
#Space: O(N)