# 005 Longest Palindromic Substring
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxL, i = 0, 0
        res = ""
        while i <= len(s):
            if 2 * (len(s) - i) < maxL: break
            left, right = i, i
            while right < len(s)-1 and s[right+1] == s[right]:
                right += 1
            i = right + 1
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            l = right - left + 1
            if l > maxL:
                maxL = l
                res = s[left:right+1]
        return res

def main():
    sol = Solution()
    print sol.longestPalindrome("babad") # "bab" or "aba"
    print sol.longestPalindrome("bbbbb") # "bbbbb"
    print sol.longestPalindrome("pwwekew") # "wekew"
if __name__ == '__main__':
    main()