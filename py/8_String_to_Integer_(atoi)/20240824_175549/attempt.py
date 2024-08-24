class Solution:
    """
    input: "   +56e-"
    input: "   5"
    input: " -005"
    input: (outside of i32 range)

    how to determine if integer is going to parse to an overflow?
    when reading in a new digit, digit * 10+ bit

    integer overflow check predicate: bound // 10 >= accumulated
    suppose the bound were 564, and string being parsed is "579" and "563"
    when you get 57, should recognize that the acccumulation must be < 56,
    or == 56 and digit <= 564 % 10.
    - track a pointer
    - first, skip past all whitespace
    - then, handle sign. Skip in any case, but track boolean `isPostive`
      bound is decided based on this bool
    - read in digits. digit = int(s[i]), result = (result*10) + digit
      zeroes are handled automatically
    - before resassigning digit, check if result > (bound // 10) or
      result == bound // 10 and digit > bound % 10. if so, return bound
    if encounter end of string or non-digit, return result

    approach:
    "   +56e-"
    "   56e-"
        i

    "   -56"
           i
    is_positive = False
    result = 56
    """

    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        result = 0
        is_positive = True

        def bound() -> int:
            max_int = (2**31) - 1
            min_int = -(2**31)
            return max_int if is_positive else min_int

        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and s[i] in set(["+", "-"]):
            if s[i] == "-":
                is_positive = False
            i += 1

        while i < len(s) and s[i].isnumeric():
            digit = int(s[i])
            if result > (abs(bound()) // 10) or (
                result == (abs(bound()) // 10) and digit > (abs(bound()) % 10)
            ):
                print("hi", result, bound())
                return bound()
            result = (result * 10) + digit
            i += 1

        return result * (1 if is_positive else -1)

