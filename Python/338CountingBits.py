# 338 Counting Bits
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0,1,1,2]
        i = 4
        while i <= num:
            for j in xrange(i):
                res.append(res[j] + 1)
            i += i
        return res[:(num+1)]

def main():
    sol = Solution()
    print sol.countBits(0) # [0]
    print sol.countBits(1) # [0,1]
    print sol.countBits(5) # [0,1,1,2,1,2]
if __name__ == '__main__':
    main()