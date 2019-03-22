# 365 Water and Jug
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x == y:
            return z == y or z == 0
        if z < 0 or z > x + y:
            return False
        # compute gcd
        a, b = x, y
        while b != 0:
            t = b
            b = a % b
            a = t
        return z % a == 0


def main():
    sol = Solution()
    print sol.canMeasureWater(3,5,4) # True
    print sol.canMeasureWater(2,6,5) # False
    print sol.canMeasureWater(3,7,8) # True
    print sol.canMeasureWater(1,1,0) # True
    #print sol.canMeasureWater(28) # "AB"
    #print sol.canMeasureWater(676) # "YZ"

if __name__ == '__main__':
    main()