class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        sub_lower = 0
        sub_upper = 0
        hidden = 0

        for diff in differences:
            hidden += diff
            if hidden > sub_upper:
                sub_upper = hidden

            if hidden < sub_lower:
                sub_lower = hidden

        sub_range = sub_upper - sub_lower
        range_ = upper - lower
        res = range_ - sub_range + 1
        
        return res if res > 0 else 0

# Time: O(N)
# Space: O(1)