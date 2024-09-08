from typing import List, Optional


class Node:
    def __init__(self) -> None:
        self.isWord: bool = False
        self.next: List[Optional[Node]] = [
            None
        ] * WordDictionary.LOWERCASE_ENG_CHAR_COUNT


class WordDictionary:
    LOWERCASE_ENG_CHAR_COUNT = 26

    # search has to match for word termination. there will be at most 2 dots in word
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not cur.next[idx]:
                cur.next[idx] = Node()
            cur = cur.next[idx]
        cur.isWord = True

    def search(self, word: str) -> bool:

        def dfs(node: Optional[Node], word_i: int) -> bool:
            if not node:
                return False
            if word_i == len(word):
                return node.isWord

            c = word[word_i]
            if c == ".":
                for branch in [b for b in node.next if b]:
                    if dfs(branch, word_i + 1):
                        return True
                return False
            idx = ord(c) - ord("a")
            if not node.next[idx]:
                return False
            return dfs(node.next[idx], word_i + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

