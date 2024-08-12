from typing import List, Optional


class Trie:
    lower_alpha_char_count: int = 26
    ascii_offset: int = 97

    class Node:
        def __init__(self):
            self.next: List[Optional[Trie.Node]] = [None] * Trie.lower_alpha_char_count
            self.is_terminal = False

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - Trie.ascii_offset
            if cur.next[i] is None:
                cur.next[i] = Trie.Node()
            cur = cur.next[i]
            assert cur
        cur.is_terminal = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - Trie.ascii_offset
            if cur is None or cur.next[i] is None:
                return False
            cur = cur.next[i]
            assert cur
        return cur.is_terminal

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - Trie.ascii_offset
            if cur is None or cur.next[i] is None:
                return False
            cur = cur.next[i]
            assert cur
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

