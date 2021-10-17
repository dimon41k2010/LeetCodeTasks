class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        inx_n, inx_t = 0,0

        while inx_n < len(name) and inx_t < len(typed):

            if name[inx_n] != typed[inx_t]:
                return(False)
            count_n, count_t = 0,0
            prev_n, prev_t = name[inx_n], typed[inx_t]
            while inx_n < len(name) and name[inx_n] == prev_n:
                count_n += 1
                inx_n += 1
            while inx_t < len(typed) and typed[inx_t] == prev_t:
                count_t += 1
                inx_t += 1
            if count_n > count_t:
                return(False)

        if inx_n != len(name) or inx_t != len(typed):
            return(False)

        return (True)

#Time: O(N+M)
#Space: O(1)