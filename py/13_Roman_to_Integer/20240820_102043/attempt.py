class Solution:
    # no need to validate!
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        possible_substract = {"I": {"V", "X"}, "X": {"L", "C"}, "C": {"D", "M"}}

        result = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c in possible_substract:
                check_next = s[i + 1] if (i + 1) < len(s) else None
                if check_next in possible_substract[c]:
                    result += values[check_next] - values[c]
                    i += 2
                    continue
            result += values[c]
            i += 1
        return result

