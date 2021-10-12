class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        d={}
        for i in range(len(magazine)):
            if magazine[i] in d.keys():
                d[magazine[i]] += 1
            else:
                d[magazine[i]] = 1
        for val in ransomNote:
            if val in d.keys():
                if d[val] == 0:
                    return False
                d[val] -= 1
            else:
                return False
        
        return True
    
#Time: O(n) + O(m) m=len(ransomNote)  = O(n)
#Space: O(m) m=len(magazine) = max 26 =  O(1)