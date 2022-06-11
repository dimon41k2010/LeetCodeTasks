class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False

        if len([char for char in password if char.islower()]) == 0:
            return False

        if len([char for char in password if char.isupper()]) == 0:
            return False

        if len([char for char in password if char.isdigit()]) == 0:
            return False

        special_char = set("!@#$%^&*()-+")
        if len([char for char in password if char in special_char]) == 0:
            return False

        if len([password[i] for i in range(len(password)-1) if password[i] == password[i+1]]) > 0:
            return False

        return True

    
#Time: O(N)
#Space: O(N)