class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # res = 0
        # for i in range(len(colors)):
        #     for j in range(1, len(colors)):
        #         if colors[i] != colors[j]:
        #             res = max(abs(i - j), res)
        # return (res)

    
#Time: O(N*2)
#Space: O(1)

#========
        return (max([abs(i - j) for i in range(len(colors)) for j in range(len(colors)) if colors[i] != colors[j]]))

#Time: O(N*2)
#Space: O(N*2)