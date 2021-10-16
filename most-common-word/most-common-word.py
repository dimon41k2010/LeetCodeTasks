class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        d = {}
        par_splitted = re.findall(r"[\w']+", paragraph)  #O(N) n = len(paragraph)
        for val in par_splitted:             #O(L) L = len(par_splitted)
            val = custom_translate(val)
            # val = val.lower().translate(str.maketrans('', '', string.punctuation))
            if val not in banned:            #O(1)
                if val in d.keys():
                    d[val] += 1
                else:
                    d[val] = 1
        max_value = 0
        res = ''
        for key in d.keys():            # O(L) L = len(val)
            if max_value < d[key]:
                max_value = d[key]
                res = key
        return res


def custom_translate(val): 
    word_list = []
    for char in val:            #O(W) W = len(val) word's length
        if char.isalpha():
            word_list.append(char.lower())   #O(1)

    return ''.join(word_list)                #O(W)

# Time: O(N) + O(L) * (O(W) + O(W) + #O(1)) + O(L) = O(N) N=all chars in the paragraph 
# Space: O(B) + O(L) + O(N)