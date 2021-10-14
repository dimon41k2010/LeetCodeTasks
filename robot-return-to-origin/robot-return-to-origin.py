class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        x = 0  #( L R )
        y = 0  #( U D )

        for command in moves:
            if command == "U":
                y += 1
            elif command == "D":
                y -= 1
            elif command == "L":
                x -= 1
            elif command == "R":
                x += 1

        if x == 0 and y == 0:
            return (True)
        return(False)

# Time: O(n)
# Space: O(1)