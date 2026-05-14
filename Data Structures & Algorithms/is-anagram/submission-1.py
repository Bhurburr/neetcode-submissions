class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {char: s.count(char) for char in set(s)}
        counts_t = {char: t.count(char) for char in set(t)}
        if counts_s == counts_t:
            return True
        return False
        