class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)

        i = -1
        for index in range(len(str_num)):
            if str_num[index] == "6":
                i = index
                break

        if i == -1:
            return(num)
        else:
            return (int(str_num[:i] + "9" + str_num[i+1:]))
        
# Time: O(N) 
# Space: O(N)


