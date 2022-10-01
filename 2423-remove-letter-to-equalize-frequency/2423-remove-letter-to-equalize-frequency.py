class Solution:
    def equalFrequency(self, word: str) -> bool:

        dic = Counter(word)
        value_dic = Counter(dic.values())
        max_value = max(dic.values())
        min_value = min(dic.values())

        if max_value == 1 or len(dic.keys()) == 1:      
            return(True)
        if len(set(value_dic.keys())) != 2:
            return (False)
        if min_value == 1 and value_dic[min_value] == 1:
            return(True)
        if value_dic[max_value] != 1:
            return(False)
        if max_value-1 not in value_dic.keys():
            return(False)
        return(True)

#Time: O(N)
#Space: O(1)