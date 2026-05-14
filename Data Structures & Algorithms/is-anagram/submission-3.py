from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for c in s:
            if c not in count_s:
                count_s[c] = 0
            count_s[c] += 1
        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        return count_s == count_t

