# note that search can contain "." character which is supposed to wildcard that character.
# which means that you need to match length
# trie would be most suitable, since it would let you just autoskip node if exists and return false otherwise
# O(n) to add and O(n) for fuzzy lookup
from typing import List, Optional


class WordDictionary:
    class Trie:
        eng_lower_count = 26

        class Node:
            def __init__(self) -> None:
                self.next: List[Optional[WordDictionary.Trie.Node]] = [
                    None
                ] * WordDictionary.Trie.eng_lower_count
                self.isWord = False

        def __init__(self) -> None:
            self.root = WordDictionary.Trie.Node()

        def insert(self, word: str) -> None:
            cur = self.root
            for c in word:
                idx = ord(c) - ord("a")
                if cur.next[idx] is None:
                    cur.next[idx] = WordDictionary.Trie.Node()
                cur = cur.next[idx]
            cur.isWord = True

        def match(self, node: Node, word: str) -> bool:
            cur = node
            for i in range(len(word)):
                c = word[i]
                if c == ".":
                    for pos in cur.next:
                        if pos is not None and self.match(pos, word[i + 1 :]):
                            return True
                    return False
                idx = ord(c) - ord("a")
                pos = cur.next[idx]
                if pos is None:
                    return False
                cur = pos
            return cur.isWord

    def __init__(self):
        self.inner = WordDictionary.Trie()

    def addWord(self, word: str) -> None:
        self.inner.insert(word)

    def search(self, word: str) -> bool:
        return self.inner.match(self.inner.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

