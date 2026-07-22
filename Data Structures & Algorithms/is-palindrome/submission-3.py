
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_text = "".join(char.lower() for char in s if char.isalnum())
        if clean_text == clean_text[::-1]:
            return True
        return False
