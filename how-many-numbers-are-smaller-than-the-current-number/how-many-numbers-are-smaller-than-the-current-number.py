class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        order_dict = {num: (len(nums)-1-i)  for i, num in enumerate(reversed(sorted(nums)))}
        return ( [order_dict[num] for num in nums ])

# Time:  O(N) + O(N log N) + O(N) = O(N log N)
# Space: O(N) + O(N) + O(N) + O(N) = O(N)