# 216 Shortest Palindrome
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in xrange(len(s)):
            if s.startswith(r[i:]):
                return r[:i] + s
        return ""

def main():
    sol = Solution()
    print sol.shortestPalindrome("") # ""
    print sol.shortestPalindrome("a") # "a"
    print sol.shortestPalindrome("aa") # "aa"
    print sol.shortestPalindrome("aba") # "aba"
    print sol.shortestPalindrome("ba") # "aba"
    print sol.shortestPalindrome("babc") # "cbabc"
    print sol.shortestPalindrome("aab") # "baab"
    print sol.shortestPalindrome("cccydcc") # "ccdycccydcc"
    print sol.shortestPalindrome("abcbaaa") # "aaabcbaaa"
    print sol.shortestPalindrome("bcbaaa") # "aaabcbaaa"
    print sol.shortestPalindrome("abca") # "acbabca"
    print sol.shortestPalindrome("abbbaba") # "ababbbaba"
    print sol.shortestPalindrome("aaaaaaaaaacdaaaaaaaaaa") # "aaaaaaaaaadcaaaaaaaaaacdaaaaaaaaaa"
if __name__ == '__main__':
    main()