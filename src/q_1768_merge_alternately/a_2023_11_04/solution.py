class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1

        i = 0
        result = ""
        while i < len(word1) and i < len(word2):
            result += word1[i] + word2[i]
            i += 1

        if len(word1) == len(word2):
            return result

        longer_word = word1 if len(word1) > len(word2) else word2
        return result + longer_word[i:]
