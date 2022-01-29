class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)    #Time: O(N)
        return [key for key in count.keys() if count[key]==1 and (key-1) not in count.keys() and (key+1) not in count.keys()]

    
# Time: O(N) + O(N) = O(N)
# Space: O(N)