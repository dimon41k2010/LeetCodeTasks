class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        grades.sort()

        res = 0
        prev_sum = 0
        prev_count = 0
        i = 0
        while i < len(grades):
            cur_sum = 0
            cur_count = 0
            while i < len(grades) and not (prev_sum < cur_sum and prev_count < cur_count):
                cur_count += 1
                cur_sum += grades[i]
                i += 1
            if prev_sum < cur_sum and prev_count < cur_count:
                res += 1
                prev_sum = cur_sum
                prev_count = cur_count
        return (res)


#Time: O(N Log N) + O(N) => O(N Log N)
#Space: O(1)

        
        