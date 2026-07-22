import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(s.lower().split())
        clean_text = clean_s.translate(str.maketrans("", "", string.punctuation))
        if clean_text == clean_text[::-1]:
            return True
        return False