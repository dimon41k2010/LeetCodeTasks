class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleKey_dict = {"type": 0, "color": 1, "name": 2}
        item_inx = ruleKey_dict[ruleKey]
        res = 0
        for i in range(len(items)):
            if ruleValue == items[i][item_inx]:
                res += 1
        return (res)

#Time: O(N)
#Space: O(3)