class Solution:
    def minTimeToType(self, word: str) -> int:
        def get_min_seconds(begin_char, end_char):  # "b" "p" == 12
            inx_begin_char = ord(begin_char) - ord("a")
            inx_end_char = ord(end_char) - ord("a")

            first_dist = abs(inx_begin_char - inx_end_char)  # 14
            second_dist = 26 - first_dist
            return min(first_dist, second_dist)

        prev = 'a'
        res = 0
        for val in word:
            res += get_min_seconds(prev, val) + 1
            prev = val
        return (res)

#Time: O(N)
#Space: O(1)