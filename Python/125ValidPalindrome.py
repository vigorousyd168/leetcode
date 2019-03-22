# 125 Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left <= right:
            while left < len(s)-1 and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1
            if left >= right:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True

def main():
    sol = Solution()
    print sol.isPalindrome("") # True
    print sol.isPalindrome("a") # True
    print sol.isPalindrome("aa") # True
    print sol.isPalindrome("aba") # True
    print sol.isPalindrome("abba") # True
    print sol.isPalindrome("aab") # False
    print sol.isPalindrome("0P") # False
if __name__ == '__main__':
    main()