# 403 Frog Jump
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # d[stone] is the set of possible units the frog can jump into stone (stones[i])
        if stones[0] != 0 or stones[1] != 1:
            return False
        d = {stone : set() for stone in stones}
        d[1].add(1)
        for x in stones[:-1]:
            for j in d[x]:
                for k in xrange(j-1, j+2):
                    if k > 0 and x+k in d:
                        d[x+k].add(k)
        return bool(d[stones[-1]])

def main():
    sol = Solution()
    print sol.canCross([0,1,3,5,6,8,12,17]) # True
    print sol.canCross([0,1,2,3,4,8,9,11]) # False
if __name__ == '__main__':
    main()