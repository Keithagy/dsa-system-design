from typing import List


class Codec:
    """
    Starting with the ASCII case, the key here is probably to escape the strings
    if you were to use a delimiter, you might mix up the delimiter with a string.
    Or, you can use an escaped repr for the encoding, and then use that character as the delimiter

    Maybe you can have the first sequence up until a dash always be the length of the string, such that you know you know you need to unescape chars
    """

    delimiter = ","
    escape_seq = "%c"
    len_delimiter = "|"

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        ["hello", ", ","world"] -> "5|2|5-hello,%c ,world"
        ["",""] -> "0|0-"
        ["","a",","] -> "0|1|1-,a,%c"
        """
        lengths = []
        for i in range(len(strs)):
            lengths.append(len(strs[i]))
            chars = []
            for c in strs[i]:
                if c == Codec.delimiter:
                    chars.append(Codec.escape_seq)
                else:
                    chars.append(c)
            strs[i] = "".join(chars)
        return (
            Codec.len_delimiter.join([str(length) for length in lengths])
            + "-"
            + Codec.delimiter.join(strs)
        )

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        lengths = []
        i = 0
        while i < len(s) and s[i] != "-":
            count = 0
            while "1" <= s[i] <= "9":
                count *= 10
                count += int(s[i])
                i += 1
            else:
                lengths.append(count)
                i += 1
        else:
            i += 1  # skip the hyphen

        j = 0
        words = s[i:].split(Codec.delimiter)
        result = []
        while j < len(lengths):
            length = lengths[j]
            if length == 0:
                result.append("")
            else:
                if j < len(words) and length != len(words[j]):
                    result.append(words[j].replace(Codec.escape_seq, Codec.delimiter))
                else:
                    result.append(words[j])
            j += 1
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
