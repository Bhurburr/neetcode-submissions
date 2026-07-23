class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        new_string = ""
        if len1 > len2:
            for i in range(len1):
                new_string += word1[i]
                if i < len2:
                    new_string += word2[i]
        else:
            for i in range(len2):
                if i < len1:
                    new_string += word1[i]
                new_string += word2[i]
        return new_string