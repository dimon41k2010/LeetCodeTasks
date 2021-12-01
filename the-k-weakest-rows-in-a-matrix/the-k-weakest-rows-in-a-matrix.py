class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        def count(arr):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == 1:  # Green zone
                    left = mid + 1
                elif arr[mid] == 0:  # Red zone
                    right = mid - 1
            return left
    
        val_lst = [count(raw) for raw in mat]   # Time: R * (log C) //
        d = {}
        for i in range (len(val_lst)):          # Time: O(R)
            if val_lst[i] not in d.keys():
                d[val_lst[i]] = [i]
            else:
                # lst = d[val_lst[i]]
                # lst.append(i)
                d[val_lst[i]].append(i)
        print (d)
        max_ones = len(mat[0])+1
        res = []
        for i in range(0, max_ones):            # Time: O(C+R)  // C=len(mat[0])
            if k == 0:
                break
            if i in d.keys():
                for val_ind in d[i]:
                    res.append(val_ind)
                    k -= 1
                    if k == 0:
                        break
            else:
                continue
        return(res)

# Time: R * (log C) + O(R) + O(C+R) = R * (log C)
# Space: O(R) + O(C)