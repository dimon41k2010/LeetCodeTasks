class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        #               0,1,2
        coord_letter = ["a","b","c","d","e","f","g","h"]  # if sum odd -> False
        #              0,1,2
        coord_digit = [1,2,3,4,5,6,7,8]   # if sum even -> True

        letter = coordinates[0]
        digit = int(coordinates[1])

        sum_inx = (coord_letter.index(letter) + coord_digit.index(digit))
        print(sum_inx)
        if sum_inx % 2 == 0:
            return (False)
        else:
            return (True)

#Time: O(1)
#Space: O(1)