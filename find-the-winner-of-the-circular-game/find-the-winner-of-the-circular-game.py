class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lst = [x for x in range(1, n+1)]  #Time: O(N) 
        start_index = 0

        def get_winner(lst, start_index, k):    #Time: O(N)
            # print(lst, start_index)
        
            if len(lst) == 1:
                return lst[0]
            
            remove_index = (start_index + k - 1) % len(lst)
            # print("remove_index", remove_index)
            lst.pop(remove_index)                   #Time: O(N) 
            start_index = (remove_index) % len(lst)
            # print("start_index", start_index)
            return get_winner(lst, start_index, k)

        return get_winner(lst, start_index, k)

#Time: O(N * N) = O(N^2) 
#Space: O(N)