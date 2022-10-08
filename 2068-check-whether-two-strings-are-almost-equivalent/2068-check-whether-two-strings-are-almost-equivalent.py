class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        dic = {}

        def add_remove_dict(word, inc, dic):
            for char in word:
                if char not in dic.keys():
                    dic[char] = inc
                else:
                    dic[char] += inc
            return dic

        add_remove_dict(word1,1, dic)
        add_remove_dict(word2,-1, dic)

        return (all([ abs(val) <= 3 for val in dic.values() ]))

#Time: O(N)
#Space: O(1)