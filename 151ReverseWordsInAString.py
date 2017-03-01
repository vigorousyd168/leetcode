# 151 Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # print s.strip().split(' ')
        # print s.strip().split()
        return ' '.join(reversed(s.strip().split()))

def main():
    sol = Solution()
    print sol.reverseWords("  the sky is  blue. ") # "blus. is sky the"

if __name__ == '__main__':
    main()