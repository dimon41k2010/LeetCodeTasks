class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_diff_time = -1
        res = None

        for i in range(len(releaseTimes)):
            diff_time = 0
            if i == 0:
                diff_time = releaseTimes[i]
            else:
                diff_time = releaseTimes[i] - releaseTimes[i-1]

            if diff_time == max_diff_time:
                res = max(res, keysPressed[i])
            elif diff_time > max_diff_time:
                max_diff_time = diff_time
                res = keysPressed[i]

        return (res)

#Time: O(N)
#Space: O(1)