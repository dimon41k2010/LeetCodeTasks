class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def hash(left,right):
            return str(left) + "#" + str(right)

        res = [0]
        visited = set()
        def recursion(arr, left, right, k_count, res):
            if left > right or k_count == 0 or hash(left,right) in visited:
                return
            res[0] += 1
            recursion(arr, left+1, right, k_count-(1 if arr[left] == k else 0), res)
            recursion(arr, left, right-1, k_count-(1 if arr[right] == k else 0), res)
            visited.add(hash(left,right))

        i = 0
        while i<len(nums):
            left = i
            k_count = 0
            while i<len(nums) and nums[i] % k == 0:
                k_count += 1 if nums[i] == k else 0
                i += 1

            recursion(nums, left, i-1, k_count, res) #

            if i < len(nums) and nums[i] % k != 0:
                i += 1
        # return res[0]

    
#Time: O(N^2)
#Space: O(N^2)

#####

        def gcd(a, b):
            if  b == 0: 
                return a
            return gcd(b , a % b)
            # Time complexity - O(log(min(a, b)) = O(log n)

        
        cnt = 0
        n = len(nums)
        
        for i in range(n):
            tmp_gcd = 0 # gcd of zero with any number is equal to the number itself
            
            for j in range(i,n):
                tmp_gcd = gcd(tmp_gcd, nums[j])
                
                if tmp_gcd == k:
                    cnt += 1
                elif tmp_gcd < k: # gcd cannot get bigger
                    break
        
        return cnt
        
        # n = nums.length
        # m = max(nums[i])

        # O( n^2 * log(m) ) - Time
        # O(1) - Space