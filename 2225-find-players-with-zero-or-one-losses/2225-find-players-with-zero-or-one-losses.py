class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        count_dict = {}
        set_ = set()

        for match in matches:
            if match[1] not in count_dict.keys():
                count_dict[match[1]] = 1
            else:
                count_dict[match[1]] += 1
            set_.update(match)

        sort_players = []
        for player in range(1, 100001):
            if player in set_:
                sort_players.append(player)

        res_1 = []
        res_2 = []
        for player in sort_players:
            if player not in count_dict.keys():
                res_1.append(player)
            elif player in count_dict.keys() and count_dict[player] == 1:
                res_2.append(player)
        return ([res_1, res_2])

# Time: O(N)
# Space: O(N)