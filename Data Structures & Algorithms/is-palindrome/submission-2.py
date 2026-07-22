
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(s.lower().split())
        clean_text = "".join(char for char in clean_s if char.isalnum())
        if clean_text == clean_text[::-1]:
            return True
        return False
