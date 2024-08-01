class Solution:
    def romanToInt(self, s: str) -> int:
        lookaheads = {
            "I": set(["V", "X"]),
            "X": set(["L", "C"]),
            "C": set(["D", "M"]),
        }

        # `token` is always either length 1 or 2
        def parse_token(token: str) -> int:
            values = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
            }
            if len(token) == 2:
                return values[token[1]] - values[token[0]]
            else:
                return values[token[0]]

        result = 0
        i = 0
        while i < len(s):
            token = s[i]
            lookahead_position = i + 1
            if token in lookaheads and lookahead_position < len(s):
                valid_modifiers = lookaheads[token]
                lookahead_char = s[lookahead_position]
                if lookahead_char in valid_modifiers:
                    token += lookahead_char
            literal = parse_token(token)
            result += literal
            characters_consumed = len(token)
            i += characters_consumed
        return result

