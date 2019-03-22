# 020 Valid Parenthese
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {')': '(', ']':'[', '}':'{'}
        for i in range(len(s)):
            b = s[i]
            if b in bracket_map.values(): # left (opening) ones
                stack.append(b)
            elif b in bracket_map.keys(): # right (closing) ones
                if len(stack) == 0 or stack[-1] != bracket_map[b]: # last bracket in stack does not match
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
def main():
    sol = Solution()
    print sol.isValid("") # True
    print sol.isValid("()") # True
    print sol.isValid("([)]") # False
    print sol.isValid("[()()]") # True
    print sol.isValid("[()(){()}]{}") # True
    print sol.isValid("[()(){()}]}") # False
if __name__ == '__main__':
    main()