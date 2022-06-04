class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        count_dict = {}
        for i in range(len(senders)):
            if senders[i] not in count_dict.keys():
                count_dict[senders[i]] = len(messages[i].split())
            else:
                count_dict[senders[i]] += len(messages[i].split())

        res = ""
        max_val = -1
        for name in count_dict.keys():
            if count_dict[name] > max_val:
                res = name
                max_val = count_dict[name]
            elif count_dict[name] == max_val:
                res = max(name, res)
        return (res)

    
#Time: O(N*M) // N=len(senders), M = len(senders[i])
#Space: O(N)