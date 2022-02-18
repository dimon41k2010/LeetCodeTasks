class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        
        beans.sort()

        pre_sum = [beans[0]]
        for i in range(1, len(beans)):
            pre_sum.append(pre_sum[-1] + beans[i])
        # print(pre_sum)
        res = sum(beans)
        for i in range(len(beans)):
            left_slide = 0
            if i > 0:
                left_slide = pre_sum[i-1]
            right_slide = 0
            if i < len(beans)-1:
                right_slide = pre_sum[-1] - pre_sum[i] - (len(beans) - i - 1) * beans[i]
            res = min(right_slide+left_slide, res)
        return (res)
    
    
# Time: O(N)
# Space: O(N)
