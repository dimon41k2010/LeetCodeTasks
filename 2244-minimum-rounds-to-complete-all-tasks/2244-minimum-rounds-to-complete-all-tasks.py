class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count_dict = {}
        for task in tasks:
            if task not in count_dict:
                count_dict[task] = 1
            else:
                count_dict[task] += 1

        res = 0
        for key in count_dict.keys():
            if count_dict[key] < 2:
                return (-1)
            elif count_dict[key] % 3 == 0:
                res += count_dict[key] // 3
            elif count_dict[key] % 3 != 0:
                res += (count_dict[key] // 3) + 1

        return(res)

#Time: O(N)
#Space: O(N)