from typing import Optional
from typing_extensions import List


class Trie:
    lowercase_eng_count = 26

    class Node:
        def __init__(self) -> None:
            self.next: List[Optional[Trie.Node]] = [
                None for _ in range(Trie.lowercase_eng_count)
            ]
            self.isWord: bool = False

    def __init__(self):
        self.root: Trie.Node = Trie.Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if cur.next[idx] is None:
                cur.next[idx] = Trie.Node()
            cur = cur.next[idx]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if cur.next[idx] is None:
                return False
            cur = cur.next[idx]
        return cur.isWord if cur else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if cur.next[idx] is None:
                return False
            cur = cur.next[idx]
        return cur is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

