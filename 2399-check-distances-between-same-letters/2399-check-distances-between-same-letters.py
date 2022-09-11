class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        last_occurrence = {}
        for i in range(len(s)):
            last_occurrence[s[i]] = i
        visited = set()
        for i in range(len(s)):
            char = s[i]
            if char in visited:
                continue
            dist = last_occurrence[char] - i - 1
            letter_index = ord(char) - ord("a")
            if dist != distance[letter_index]:
                return(False)
            visited.add(char)
        return (True)

#Time: O(N)
#Space: O(1)
