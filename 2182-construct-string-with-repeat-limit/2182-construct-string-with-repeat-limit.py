class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        letter = "z"
        
        # print(ord(letter))
        # print(chr(ord('a')-1))
        res = []
        back_up_letter = None
        while ord(letter) >= ord('a'):

            if letter in count.keys():
                is_break = False
                is_backup = False
                for _ in range(repeatLimit):
                    res.append(letter)
                    count[letter] -= 1
                    if count[letter] == 0:
                        count.pop(letter)
                        is_break = True
                    if back_up_letter:
                        letter = back_up_letter
                        back_up_letter = None
                        is_backup = True
                        is_break = True
                    if is_break:
                        break
                if is_backup:
                    continue
                if letter in count.keys():
                    back_up_letter = letter

            letter = chr(ord(letter)-1)

        return (''.join(res))
    
    
# Time: O(N)
# Space: O(1)
    
    