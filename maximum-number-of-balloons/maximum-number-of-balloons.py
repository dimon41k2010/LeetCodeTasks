class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
     
        d_text = convert_to_dict(text)
        d_goal = convert_to_dict("balloon")
        res = len(text)

        for key in d_goal.keys():       # O(5)
            if key in d_text.keys():    # O(1)
                res = min(res, d_text[key] // d_goal[key])
            else:
                res = 0
                break
        return (res)

        
def convert_to_dict(data):  #O(N)
    d = {}
    for i in range(len(data)):
        if data[i] in d.keys():
            d[data[i]] += 1
        else:
            d[data[i]] = 1
    return d


#Time: O(N) + O(4) + O(1) = O(N) // N=len(text)
#Space: O(26) + O(5) = O(1)