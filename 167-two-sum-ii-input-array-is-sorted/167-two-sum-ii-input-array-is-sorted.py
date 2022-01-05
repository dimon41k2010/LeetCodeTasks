class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        res2 = []
        while left != right:
            s = numbers[left] + numbers[right]
            if s == target:
                res2.extend([left+1, right+1])
                break
            elif s > target:
                right -= 1
            else:
                left += 1
    
        return res2
    # Time: O(n)
    # Space: O(1)
    
    # Second solution (refactored)
        res = []
        for i in range(0, len(numbers)):
            for k in range(i+1, len(numbers)):
                if numbers[i] + numbers[k] == target:
                    res.extend([i+1,k+1])
        return res

# Time: O(n2) | O(N log n) -> Sorting
# Space: O(1)