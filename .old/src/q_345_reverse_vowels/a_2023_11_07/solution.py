from collections import deque


class Solution2:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        front = 0
        back = len(s) - 1
        result = list(s)

        while front < back:
            while result[front].lower() not in vowels and front < back:
                front += 1
            while result[back].lower() not in vowels and front < back:
                back -= 1
            result[front], result[back] = result[back], result[front]
            front += 1
            back -= 1
        return "".join(result)


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        vowels_stack = []
        consonant_fragments = deque()
        current_consonant_fragment = ""
        for i in range(len(s)):
            if s[i].lower() in vowels:
                consonant_fragments.append(current_consonant_fragment)
                current_consonant_fragment = ""
                vowels_stack.append(s[i])
            else:
                current_consonant_fragment += s[i]
        if len(current_consonant_fragment) != 0:
            consonant_fragments.append(
                current_consonant_fragment
            )  # introduces possibility that consonant_fragments is longer by 1
            current_consonant_fragment = ""
        result = ""
        while len(consonant_fragments) != 0 and len(vowels_stack) != 0:
            result += consonant_fragments.popleft() + vowels_stack.pop()

        while len(consonant_fragments) > 0:
            result += consonant_fragments.popleft()
        return result
