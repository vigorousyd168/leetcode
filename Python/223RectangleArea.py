# 223 Rectangle Area
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # common part:
        # x: max(A,E) ~ min(C,G)
        # y: max(B,F) ~ min(D,H)
        if E > C or A > G or F > D or B > H:
            return (C-A)*(D-B) + (G-E)*(H-F)
        return (C-A)*(D-B) + (G-E)*(H-F) - (min(C,G)-max(A,E)) * (min(D,H)-max(B,F))
def main():
    sol = Solution()
    print sol.computeArea(-3,0,3,4,0,-1,9,2) # 45
    print sol.computeArea(0,0,0,0,-1,-1,1,1) # 4

if __name__ == '__main__':
    main()