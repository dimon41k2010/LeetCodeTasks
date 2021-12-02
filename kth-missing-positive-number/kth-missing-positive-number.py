class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        index = -1
        missign_count = 0

        for i in range(len(arr)):   # Time: O(n)
            nun_count = i + 1
            missign_count = arr[i] - nun_count
            if missign_count >= k:
                index = i
                break

        if index == -1:
            diff = k - missign_count - 1
            next_missing_number = arr[-1] + 1
            return (next_missing_number + diff)
        else:
            prev_missing_number = arr[index] - 1
            diff = missign_count - k
            return (prev_missing_number - diff)

# Time: O(n)
# Space: O(1)