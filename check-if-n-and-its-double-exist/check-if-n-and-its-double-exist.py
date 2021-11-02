class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # set_ = set(arr)
        # for num in arr:
        #     if num * 2 in set_:
        #         return(True)
        # return False

#Second solution 
        if arr.count(0) > 1:
            return (True)   
        set_ = set(arr)
        return (len([ num for num in arr if num != 0 and (num * 2) in set_ ]) > 0)

# Time: O(N)
# Space: O(N)