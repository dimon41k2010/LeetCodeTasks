class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        storage = {}

        def add_to_storage(items):
            for item in items:
                [key, value] = item
                if key in storage.keys():
                    storage[key] += value
                else:
                    storage[key] = value

# print(add_to_storage(items1))
# add_to_storage(storage,items1)
# add_to_storage(storage,items2)

        list_items = [items1, items2]
        for items in list_items:
            add_to_storage(items)

        res = []
        for key in range(1001):
            if key in storage.keys():
                res.append([key, storage[key]])
        return (res)

#Time: O(N)
#Space: O(N)