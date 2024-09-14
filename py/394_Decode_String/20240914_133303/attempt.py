class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        cur_frag = []

        count_stack = []
        cur_count = 0
        for c in s:
            if c.isalpha():
                cur_frag.append(c)
                continue
            if c.isdigit():
                cur_count = cur_count * 10 + int(c)
                continue
            if c == "[":
                str_stack.append(cur_frag)
                cur_frag = []
                count_stack.append(cur_count)
                cur_count = 0
                continue
            if c == "]":
                cur_frag *= count_stack.pop()
                outer = str_stack.pop()
                outer.extend(cur_frag)
                cur_frag = outer
        str_stack.extend(cur_frag)
        return "".join(["".join(s) for s in str_stack])

