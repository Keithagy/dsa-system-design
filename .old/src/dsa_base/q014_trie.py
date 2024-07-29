from __future__ import annotations
import unittest

from typing import List, Optional


class Node:
    children: List[Optional[Node]]
    is_word: bool

    def __init__(self) -> None:
        self.children = [None] * Trie.alphabet_len
        self.is_word = False


# This will ignore casing.
class Trie:
    alphabet_len = 26
    start: Node

    def __init__(self) -> None:
        self.start = Node()

    def _calc_index_for_c(self, c: str) -> int:
        # `c` must be only a single character between A/a to Z/z!
        return ord(c.lower()) - ord("a")

    def _calc_char_for_i(self, i: int) -> str:
        # `i` must be between 0 and Trie.alphabet_len
        return chr(i + ord("a"))

    def insert(self, new_word: str) -> None:
        cur = self.start
        for c in new_word:
            i = self._calc_index_for_c(c)
            if not cur.children[i]:
                cur.children[i] = Node()
            cur = cur.children[i]
        cur.is_word = True

    def delete(self, word: str) -> None:
        cur = self.start
        for c in word:
            i = self._calc_index_for_c(c)
            if not cur.children[i]:
                return  # nothing to delete
            cur = cur.children[i]
        cur.is_word = False
        # This is a simple implementation. You might want to prune the trie depending on whether this is a terminal node

    def check(self, word: str) -> bool:
        cur = self.start
        for c in word:
            i = self._calc_index_for_c(c)
            if not cur.children[i]:
                return False
            cur = cur.children[i]
        return cur.is_word

    # what's the next-nearest word? autocomplete
    def complete(self, substring: str) -> str:
        result = []
        cur = self.start
        for c in substring:
            i = self._calc_index_for_c(c)
            if not cur.children[i]:
                return ""  # this substring does not exist in the trie
            result.append(c)
            cur = cur.children[i]

        if cur.is_word:
            return substring

        while not cur.is_word:
            for j in range(len(cur.children)):
                if not cur.children[j]:
                    continue
                cur = cur.children[j]
                result.append(self._calc_char_for_i(j))
                break  # naively autocomplete based on alphabetical order
                # NOTE: you should never encounter a case where you interate completely through children and they are all None, but the node itself is not a word.
        return "".join(result)


class TestTrie(unittest.TestCase):
    def test_insert_and_check(self):
        trie = Trie()
        trie.insert("hello")
        self.assertTrue(trie.check("hello"))
        self.assertFalse(trie.check("world"))

    def test_delete(self):
        trie = Trie()
        trie.insert("test")
        trie.delete("test")
        self.assertFalse(trie.check("test"))

    def test_complete(self):
        trie = Trie()
        trie.insert("henlo")
        trie.insert("helld")
        trie.insert("helicopter")
        trie.insert("help")
        self.assertEqual(trie.complete("hell"), "helld")
        self.assertEqual(trie.complete("helic"), "helicopter")
        self.assertEqual(trie.complete("hen"), "henlo")

    def test_autocomplete_no_match(self):
        trie = Trie()
        trie.insert("test")
        self.assertEqual(trie.complete("a"), "")

    def test_autocomplete_exact_word(self):
        trie = Trie()
        trie.insert("test")
        self.assertEqual(trie.complete("test"), "test")

    def test_insert_case_insensitivity(self):
        trie = Trie()
        trie.insert("TeSt")
        self.assertTrue(trie.check("test"))
        self.assertTrue(trie.check("Test"))
        self.assertTrue(trie.check("tEsT"))

    def test_delete_nonexistent_word(self):
        trie = Trie()
        trie.delete("nonexistent")
        # Just ensuring no exception is raised


if __name__ == "__main__":
    unittest.main()
