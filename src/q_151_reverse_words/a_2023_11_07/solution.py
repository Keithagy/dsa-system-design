from collections import deque
from typing import Deque


class Solution:
    def reverseWords(self, s: str) -> str:
        words: Deque[str] = deque()
        current_word = ""
        for c in s:
            if c == " ":
                if len(current_word) == 0:
                    continue
                words.appendleft(current_word)
                current_word = ""
                continue
            current_word += c
        if len(current_word) != 0:
            words.appendleft(current_word)
        return " ".join(words)
