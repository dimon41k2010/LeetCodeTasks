class Solution:
    def defangIPaddr(self, address: str) -> str:
        #stream
#         length = len(address)
#         for i in range(length):
#             if address[i] != '.':
#                 address += address[i]
#             else:
#                 address += '[.]'
#         return address[length:]
    
        return('[.]'.join(address.split(".")))