class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = ''
        charList = list(s) # create a list of char from a string
        l = len(charList)
        if l == 1:
            return s
        # operator % for modular division in Python
        # operator / for division (when both args are int)
        # s is string, not list of chars. That assumption would lead to: 'unicode' object does not support item assignment
        for i in range(0, l/2):
            temp = charList[i]
            charList[i] = charList[l-1-i]
            charList[l-1-i] = temp
        return ''.join(charList) # create a string from a list of char

def main():
    sol = Solution()
    print sol.method(args)

if __name__ == '__main__':
    main()