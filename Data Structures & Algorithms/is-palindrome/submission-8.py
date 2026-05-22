class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s.replace(" ", "").lower() if char.isascii() and char.isalnum())
        f = 0
        b = len(s) - 1

        while f < b:
            if s[f] != s[b]:
                return False
            f += 1
            b -= 1
        return True
