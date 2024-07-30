class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        stock = {}  # max size of 26 (constant), since only lowercase english
        for avail in magazine:
            stock[avail] = stock.setdefault(avail, 0) + 1

        for needed in ransomNote:
            if needed not in stock:
                return False
            stock[needed] = stock[needed] - 1
            if stock[needed] == 0:
                del stock[needed]
        return True

