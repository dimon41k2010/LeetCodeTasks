class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def valid_price(word):  # O(W)
            if len(word) > 1 and word[0] == "$" and all([char.isdigit() for char in word[1:] ]):
                return True
            return False

        words = sentence.split()
        res_list = []
        for word in words:
            if valid_price(word):
                price = float(word[1:])
                percent = (100 - discount) / 100
                price *= percent
                res_list.append("${:.2f}".format(price))
            else:
                res_list.append(word)
        return (" ".join(res_list))

#Time: O(N)
#Space: O(N)