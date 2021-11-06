class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        last_planted = -1
        for i in range(len(flowerbed)):
            val = flowerbed[i]
            if val == 1:
                continue
            is_left_plod = i - 1 < 0 or (flowerbed[i-1] == 0 and i-1 != last_planted)
            is_right_plod = i + 1 >= len(flowerbed) or flowerbed[i+1] == 0
            if is_left_plod and is_right_plod:
                count += 1
                last_planted = i
        if count >= n:
            return True
        else:
            return False
        
#Time: O(n)
#Space: O(1)