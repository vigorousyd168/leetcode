class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        # neg number is NOT palindrome...
        if x < 0:
            return False
        temp = x
        while (temp != 0):
            rev = rev * 10 + temp%10
            temp = temp/10
        return x == rev
def main():
    sol = Solution()
    print 2**31
    print sol.isPalindrome(12) # False
    print sol.isPalindrome(-12321) # True
    print sol.isPalindrome(0) # True
    print sol.isPalindrome(-2147447412) # False

if __name__ == '__main__':
    main()