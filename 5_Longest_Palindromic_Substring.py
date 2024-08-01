class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        start, length = 0, 1
        for i in range(1, len(s)):
            L, R = i - length, i + 1
            s1 = s[L-1 : R]
            if L >= 1 and s1 == s1[::-1]:
                length += 2
                start = L - 1
            else:
                s2 = s[L:R]
                if s2 == s2[::-1]:
                    length += 1
                    start = L
        return s[start:start + length]