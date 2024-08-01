class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        t, n = 0, 1
        for i in range(1, len(s)):
            l, r = i - n, i + 1
            s1 = s[l-1 : r]
            if l >= 1 and s1 == s1[::-1]:
                n += 2
                t = l - 1
            else:
                s2 = s[l:r]
                if s2 == s2[::-1]:
                    n += 1
                    t = l
        return s[t:t+n]