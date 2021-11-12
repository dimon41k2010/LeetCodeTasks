rows = [set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
     
        res = []
        for word in words:
            if check_word(word.lower()):
                res.append(word)

        return res
        
def get_row(letter):
    for i in range(len(rows)):    
        if letter in rows[i]:
            return rows[i]

def check_word(word):
    row = get_row(word[0])
    # print(word)
    for letter in word:
        # print(letter)
        if letter not in row:
            return False
    return True

#Time: O(words) * O(word) = O(n2)
#Space: O(1)



        
#         keyMap = {}
#         for key in "qwertyuiopQWERTYUIOP":
#             keyMap[key] = 0
#         for key in "asdfghjklASDFGHJKL":
#             keyMap[key] = 1
#         for key in "zxcvbnmZXCVBNM":
#             keyMap[key] = 2
            
#         ans = []
#         for word in words:
#             rowNum = keyMap[word[0]]
#             for char in word:
#                 if keyMap[char] != rowNum:
#                     break
#             else:
#                 ans.append(word)
                
#         return ans
    # Time: O(n), Space: O(1) (Except for answer)