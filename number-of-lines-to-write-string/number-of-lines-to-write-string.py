class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        sum_pix = 0
        lines = 1
        for char in s:
            inx = ord(char) - ord("a")
            width = widths[inx]
            if sum_pix + width <= 100:
                sum_pix += width
            else:
                lines += 1
                sum_pix = width

        return [lines,sum_pix]
    
# Time: O(n)
# Space: O(1)