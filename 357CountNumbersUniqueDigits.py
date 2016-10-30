# 357 Count Numbers with Unique Digits
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [1,10]
        if n <= 1:
            return count[n]
        if n > 10:
            n = 10
        currCount = 9
        for i in range(2, n+1):
            currCount = currCount * (11-i)
            count.append(count[-1] + currCount)
        return count[n]
def main():
    sol = Solution()
    print sol.countNumbersWithUniqueDigits(0) # 1
    print sol.countNumbersWithUniqueDigits(1) # 10
    print sol.countNumbersWithUniqueDigits(2) # 91
    print sol.countNumbersWithUniqueDigits(4) # 5275
    print sol.countNumbersWithUniqueDigits(10) # 8877691
    print sol.countNumbersWithUniqueDigits(11) # 8877691

if __name__ == '__main__':
    main()