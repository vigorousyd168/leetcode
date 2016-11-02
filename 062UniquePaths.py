# 062 Unique Paths
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # just compute the a!/((a-b)!b!) where a = m+n-2 and b = n-1
        if m <= 0 or n <= 0:
            return 0
        fact = [1]
        for i in range(1, m+n-1):
            fact.append(fact[-1] * i)
        return fact[-1]//fact[n-1]//fact[m-1]
        
def main():
    sol = Solution()
    print (sol.uniquePaths(3, 7)) # 28
if __name__ == '__main__':
    main()