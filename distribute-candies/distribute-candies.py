class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        #candyType = [1,1,2,2,3,3] #3
         #candyType = [1,2,3,4,5,6,7] #6 / 2 = 3
        return min(len(set(candyType)),len(candyType)//2)
    
    #Time: O(n)
    #Space: O(n)