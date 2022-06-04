class Solution:
    def digitCount(self, num: str) -> bool:
        
        count_dict = Counter(num)

        for index_and_key in range(len(num)):
            prediction = int(num[index_and_key])
            index_and_key = str(index_and_key)
            original = 0 if index_and_key not in count_dict.keys() else count_dict[index_and_key]

            if prediction != original:
                return (False)

        return(True)

    
#Time: O(N)
#Space: O(N)