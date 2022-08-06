class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutation = []
        visited = set()
        res = []

        def func(permutation,nums,visited,res):
            if len(permutation) == len(nums):
                res.append(permutation.copy())

            for i in range(len(nums)):
                if i not in visited:
                    permutation.append(nums[i])
                    visited.add(i)
                    
                    func(permutation,nums,visited,res)
                    
                    permutation.remove(nums[i])
                    visited.remove(i)

        func(permutation,nums,visited,res)
        return(res)
    
#Time: O(N^N) / N=len(nums)
#Space: O(N) / N=len(nums)