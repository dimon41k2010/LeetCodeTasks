class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        words = text.split()
        if len(words) < 2:
            return words[0] + (' ' * spaces)
        spaces_between = spaces // (len(words)-1)
        spaces_end = spaces % (len(words)-1)
        return  (spaces_between * ' ').join(words) + (spaces_end * " ")

#Time: O(N)
#Space: O(N)