class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = {'N' : [0,1], 'S':[0,-1], 'E': [1,0], 'W': [-1,0]}
        tail = set()
        x, y = 0, 0
        tail.add(str(x) + "#" + str(y))
        for val in path: # O(N)
            n_x, n_y = d[val]
            x += n_x
            y += n_y
            coord = str(x) + "#" + str(y)
            if coord not in tail:
                tail.add(coord)
            else:
                return(True)
        return (False)


#Time: O(N)
#Space: O(N) + O(4)  // N=len(tail)