class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
            
            
            
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        return(candies)             # rewriting to the same list

#Time: O(N)
#Space: O(1)
    

    # 2nd better solution using list comprehension

        max_candies = max(candies)
        return ([ "true1" if candy+extraCandies >= max_candies else "false" for candy in candies ])
        
#Time: O(N^2)
#Space: O(N)