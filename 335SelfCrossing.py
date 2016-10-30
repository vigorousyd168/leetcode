# 335 Self Crossing
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        a = [0] * 7 # x
        b = [0] * 7 # y
        maxA, maxB, minA, minB = 0, 0, 0, 0
        inward = False
        idx = 0
        for i in range(len(x)):
            nextIdx = (idx+1)%7
            check = inward
            if i % 4 == 0:
                a[nextIdx] = a[idx]
                b[nextIdx] = b[idx] + x[i]
                if b[nextIdx] > maxB:
                    maxB = b[nextIdx]
                else:
                    inward = True
            elif i % 4 == 1:
                a[nextIdx] = a[idx] - x[i]
                b[nextIdx] = b[idx]
                if a[nextIdx] < minA:
                    minA = a[nextIdx]
                else:
                    inward = True
            elif i % 4 == 2:
                a[nextIdx] = a[idx]
                b[nextIdx] = b[idx] - x[i]
                if b[nextIdx] < minB:
                    minB = b[nextIdx]
                else:
                    inward = True
            else:
                a[nextIdx] = a[idx] + x[i]
                b[nextIdx] = b[idx]
                if a[nextIdx] > maxA:
                    maxA = a[nextIdx]
                else:
                    inward = True
            if inward:
                #print a[nextIdx], a[(idx-4)%7], a[idx], a[(idx-5)%7]
                #print b[nextIdx], b[(idx-4)%7], b[idx], b[(idx-5)%7]
                if (a[nextIdx] - a[(idx-4)%7]) * (a[idx] - a[(idx-5)%7]) <= 0 and (b[nextIdx] - b[(idx-4)%7])*(b[idx] - b[(idx-5)%7]) <= 0:
                    return True
                if (a[nextIdx] - a[(idx-2)%7]) * (a[idx] - a[(idx-3)%7]) <= 0 and (b[nextIdx] - b[(idx-2)%7])*(b[idx] - b[(idx-3)%7]) <= 0:
                    return True
            idx = nextIdx
        return False

def main():
    sol = Solution()
    print sol.isSelfCrossing([1,1,1,1]) # True
    print sol.isSelfCrossing([1,2,3,4]) # False
    print sol.isSelfCrossing([2,1,1,2]) # True
    print sol.isSelfCrossing([]) # False
    print sol.isSelfCrossing([1,2,3]) # False
    print sol.isSelfCrossing([1,1,2,2,3,3,4,4,4,1]) # True
    print sol.isSelfCrossing([3,3,4,2,2]) # False

if __name__ == '__main__':
    main()