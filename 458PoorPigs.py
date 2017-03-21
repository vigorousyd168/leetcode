# 458 Poor Pigs
import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets <= 1 or minutesToTest < minutesToDie:
            return 0
        if minutesToDie == 0:
            return 1
        rounds = math.floor(float(minutesToTest)/minutesToDie)
        digits = math.ceil(math.log(buckets, rounds+1))
        # each pig can be used to find one digit in n (n represented using (rounds+1)-ary)
        return int(digits)
def main():
    sol = Solution()
    print sol.poorPigs(1000, 15, 60) # 5
    print sol.poorPigs(1000, 12, 60) # 4
    print sol.poorPigs(100, 10, 10) # 7
    print sol.poorPigs(500, 24, 48)
if __name__ == '__main__':
    main()