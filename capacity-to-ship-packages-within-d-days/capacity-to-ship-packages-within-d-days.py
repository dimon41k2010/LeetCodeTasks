class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def possible_capacity(capacity):
            single_ship = 0
            counter = 0

            for weight in weights:
                # print("this ",single_ship, weight,counter)
                if single_ship + weight <= capacity:
                    single_ship += weight
                else:
                    counter += 1
                    single_ship = weight
                    if counter > days:
                        return False
                if counter == days:
                    return False
                # print(single_ship, weight,counter)
            return True

        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if possible_capacity(mid):   # if True
                right = mid - 1
            else:                       # if NOT True
                left = mid + 1
        return(left)
    
#Time: O(log N) * O(N) = O(N log N)
#Space: O(1)
