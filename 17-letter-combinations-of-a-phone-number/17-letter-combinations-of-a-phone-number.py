class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        queue = [""]

        for digit in digits:
            new_queue = []
            for item in queue:
                for letter in letters[digit]:
                    new_queue.append(item + letter)
            queue = new_queue
        return (queue)

#Time: O(4^N)
#Space: O(4^N * N)