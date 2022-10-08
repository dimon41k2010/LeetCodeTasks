class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        count = 0 
        current = set() 
        for i in range(len(word)):
            if word[i] in 'aeiou':
                current.add(word[i])
                
                for j in range(i+1, len(word)): 
                    if word[j] in 'aeiou':
                        current.add(word[j])
                    else:
                        break
                    
                    if len(current) == 5:
                        count += 1
						
            current = set()
                        
        return count
    
#Time: O(N)
#Space: O(1)

# second solution
        unique_vowels = set(['a', 'e', 'i', 'o', 'u'])

        def is_valid(count_dict):
            for vowel in unique_vowels:
                if vowel not in count_dict.keys():
                    return False
            return True

        def add_to_counter(count_dict, key):
            if key in count_dict.keys():
                count_dict[key] += 1
            else:
                count_dict[key] = 1
        res = 0

        for i in range(len(word)):
            count_dict = {}
            while not is_valid(count_dict) and i < len(word) and word[i] in unique_vowels:
                add_to_counter(count_dict, word[i])
                i += 1
            while is_valid(count_dict) and i < len(word) and word[i] in unique_vowels:
                res += 1
                i += 1
            if is_valid(count_dict):
                res += 1
        return (res)

#Time: O(N)
#Space: O(1)