from typing import List, Optional


class Trie:
    lowercase_eng_letter_count: int = 26
    ascii_offset: int = 97

    class Node:
        def __init__(self, val: str, terminal: bool) -> None:
            self.val = val
            self.next: List[Optional[Trie.Node]] = [
                None
            ] * Trie.lowercase_eng_letter_count
            self.terminal = terminal

    def __init__(self):
        self.root = Trie.Node("", False)

    def insert(self, word: str) -> None:
        prev = self.root
        for c in word:
            idx = ord(c) - Trie.ascii_offset
            if not prev.next[idx]:
                prev.next[idx] = Trie.Node(c, False)
            prev = prev.next[idx]
        prev.terminal = True

    def search(self, word: str) -> bool:
        prev = self.root
        for c in word:
            idx = ord(c) - Trie.ascii_offset
            if not prev.next[idx]:
                return False
            prev = prev.next[idx]
        return prev.terminal

    def startsWith(self, prefix: str) -> bool:
        prev = self.root
        for c in prefix:
            idx = ord(c) - Trie.ascii_offset
            if not prev.next[idx]:
                return False
            prev = prev.next[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

