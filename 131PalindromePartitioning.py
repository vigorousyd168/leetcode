# 131 Palindrome Partitioning
class Solution(object):
    def isPalindrome(self, ss):
        start, end = 0, len(ss)-1
        while start < end:
            if ss[start] != ss[end]:
                return False
            start, end = start + 1, end - 1
        return True
    def dfs(self, idx):
        if idx == len(self.s):
            self.ret.append(self.path)
        for i in xrange(idx, len(self.s)):
            if self.isPalindrome(self.s[idx: i+1]):
                self.path.append(self.s[idx: i+1])
                self.dfs(i+1)
                self.path = self.path[:-1]
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.path = []
        self.ret = []
        self.s = s
        self.dfs(0)
        return self.ret

def main():
    sol = Solution()
    print sol.partition("abb") # [["a","a","b"],["aa","b"]]
if __name__ == '__main__':
    main()