class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        count_d = {}        # Time: O(N)
        for word in words:
            if word in count_d.keys():
                count_d[word] += 1
            else:
                count_d[word] = 1

        res = 0
        is_used = False
        for key in count_d.keys():          # Time: O(1)
            if key[0] != key[1]:
                reversed_key = key[::-1]
                if reversed_key not in count_d.keys():
                    continue
                used_pair_count = min(count_d[key], count_d[reversed_key])
                res += 4 * used_pair_count
                count_d[key] -= used_pair_count
                count_d[reversed_key] -= used_pair_count
            elif key[0] == key[1]:
                if count_d[key] >= 2:
                    used_pair_count_2 = count_d[key] // 2
                    res += used_pair_count_2 * 4
                    count_d[key] -= used_pair_count_2 * 2
                if count_d[key] == 1 and not is_used:
                    res += 2
                    is_used = True
        return res

# Time: O(N) + O(1)
# Space: O(1)