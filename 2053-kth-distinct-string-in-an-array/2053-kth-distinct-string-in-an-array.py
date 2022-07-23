class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        distinct = Counter(arr)

        counter = 0
        for char in arr:
            if distinct[char] == 1:
                counter += 1
            if counter == k:
                return (char)
        return("")

    
#Time: O(N)
#Space: O(1)