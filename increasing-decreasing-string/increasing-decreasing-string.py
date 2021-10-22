class Solution:
    def sortString(self, s: str) -> str:
        used = [False for _ in s]
        res = []
        count = 0

        while count != len(s):
            is_found = True
            char_min = "`"
            while is_found:
                is_found = False
                smallest = "{"
                inx = -1
                for i in range(len(s)):
                    if not used[i]:
                        if s[i] > char_min and s[i] < smallest:
                            smallest = s[i]
                            inx = i
                            is_found = True
                if is_found:
                    res.append(s[inx])
                    used[inx] = True
                    count += 1
                    char_min = s[inx]

            is_found = True
            char_max = "{"
            while is_found:
                is_found = False
                biggest = "`"
                inx = -1
                for i in range(len(s)):
                    if not used[i]:
                        if s[i] < char_max and s[i] > biggest:
                            biggest = s[i]
                            inx = i
                            is_found = True
                if is_found:
                    res.append(s[inx])
                    used[inx] = True
                    count += 1
                    char_max = s[inx]

        return (''.join(res))
        