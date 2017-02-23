# 058 Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, lastCount = 0, 0
        for c in s:
            if c != ' ':
                count += 1
                lastCount = count
            else:
                count = 0
        return lastCount

def main():
    sol = Solution()
    print sol.lengthOfLastWord("Hel lo") # 2
    print sol.lengthOfLastWord("") # 0
    print sol.lengthOfLastWord("h ") # 1
    print sol.lengthOfLastWord(" hello") # 5
if __name__ == '__main__':
    main()