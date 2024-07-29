from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        current_char_start = 0
        current_char_end = 0
        current_char = ""
        input_arr_len = len(chars)
        i = 0
        while i < input_arr_len:
            char = chars[i]
            if char != current_char:
                # Modify input array with compressed chars
                prev_char_count = current_char_end - current_char_start + 1
                if prev_char_count > 1:
                    prev_char_count_str = str(prev_char_count)
                    for j in range(len(prev_char_count_str)):
                        count_digit = prev_char_count_str[j]
                        # write over one of the repeated chars with a digit
                        # we will always have at least as many repeated chars as digits
                        chars[current_char_start + j + 1] = count_digit

                    # Remove trailing chars
                    del chars[current_char_start + 1 + len(prev_char_count_str) : i]
                    input_arr_len = len(chars)
                    i = current_char_start + len(prev_char_count_str) + 1
                # Reset for new character
                current_char = char
                current_char_start = i
                current_char_end = i
            else:
                current_char_end = i
            i += 1

        if current_char_end > current_char_start:
            # Modify input array with compressed chars
            prev_char_count = current_char_end - current_char_start + 1
            prev_char_count_str = str(prev_char_count)
            for j in range(len(prev_char_count_str)):
                count_digit = prev_char_count_str[j]
                # write over one of the repeated chars with a digit
                # we will always have at least as many repeated chars as digits
                chars[current_char_start + j + 1] = count_digit

            # Remove trailing chars
            del chars[current_char_start + 1 + len(prev_char_count_str) : i]
        return len(chars)
