class Solution:
    def interpret(self, command: str) -> str:
        res = []
        for i in range(len(command)):
            if command[i:i+4] == "(al)":
                res.append("al")
            elif command[i:i+2] == "()":
                res.append("o")
            elif command[i] == "G":
                res.append("G")

        return (''.join(res))

#Time: O(N)
#Space: O(N)