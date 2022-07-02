class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()

        res = 0
        for i in range(len(seats)):
            diff = abs(students[i] - seats[i])
            res += diff
        return(res)

#Time: O(N Log N)
#Space: O(1)