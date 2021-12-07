

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
#         lst = [x for x in range(1, n+1)]  #Time: O(N) 
#         start_index = 0

#         def get_winner(lst, start_index, k):    #Time: O(N)
#         # print(lst, start_index)

#             if len(lst) == 1:
#                 return lst[0]

#             remove_index = (start_index + k - 1) % len(lst)
#             # print("remove_index", remove_index)
#             lst.pop(remove_index)                   #Time: O(N) 
#             start_index = (remove_index) % len(lst)
#             # print("start_index", start_index)
#             return get_winner(lst, start_index, k)
        
        
#         return get_winner(lst, start_index, k)
    
    
#Time: O(N * N) = O(N^2) 
#Space: O(N)


# === 2nd Solution using Queue

        queue = [x for x in range(1, n+1)]  #Time: O(N)
        # print(queue)
        while len(queue) != 1:
            j = 1
            while j <= k-1:
                queue.append(queue.pop(0))
                # print("queue.append",queue)
                j += 1
            queue.pop(0)
        return queue[0]

#Time: O(N * M) // N -> n, M -> k
#Space: O(N)