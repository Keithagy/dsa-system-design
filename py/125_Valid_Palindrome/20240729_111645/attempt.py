class Solution:

    def isPalindrome(self, s: str) -> bool:
        forward = 0
        backward = len(s) - 1

        while forward < backward:
            while forward < backward and not s[forward].isalnum():
                forward = forward + 1

            while backward > forward and not s[backward].isalnum():
                backward = backward - 1

            if s[forward].lower() != s[backward].lower():
                return False

            forward = forward + 1
            backward = backward - 1

        return True

