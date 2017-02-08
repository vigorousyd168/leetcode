# 354 Russian Doll Envelopes
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # sort on width (asc), height (desc)
        envs = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        nums = [env[1] for env in envs]
        # LIS on nums
        n = len(nums)
        l = 0
        M = [0]* (n+1)
        for i in xrange(n):
            lo = 1
            hi = l
            while lo <= hi:
                mid = (lo + hi + 1)/2
                if nums[M[mid]] < nums[i]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            newL = lo
            M[newL] = i
            if newL > l:
                l = newL
        return l

def main():
    sol = Solution()
    print sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) # 3
    print sol.maxEnvelopes([]) # 0
if __name__ == '__main__':
    main()