class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        sum_ = sum(distance) #Time: O(N)

        if start > destination:
            start, destination = destination, start

            
        def recur_sum(distance, start, destination):  #Time: O(N)
            if start >= destination:
                return 0
            res = distance[start]
            res += recur_sum(distance, start + 1, destination)

            return res

        yellow = recur_sum(distance, start, destination)
        blue = sum_ - yellow

        return (min(blue, yellow))

#Time: O(N) + O(N) = O(N) 
#Space: O(N)