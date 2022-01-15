class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:  
        
        for i in (range(len(digits)-1,-1,-1)):           
            # print(digits[i])
            if digits[i] == 9: 
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else: 
                digits[i] = digits[i] +1
                break
        return digits 
    
    #Time: O(n) + O(1) + O(n)
    #Space: O(n)