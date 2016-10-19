# 168 Excel Sheet Column Title
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = 26
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        title = ""
        while 1:
            title = letters[(n-1)%base] + title
            newN = (n-1)/base
            if newN == 0:
                return title
            else:
                n = newN
def main():
    sol = Solution()
    print sol.convertToTitle(1) # "A"
    print sol.convertToTitle(3) # "C"
    print sol.convertToTitle(26) # "Z"
    print sol.convertToTitle(27) # "AA"
    print sol.convertToTitle(28) # "AB"
    print sol.convertToTitle(676) # "YZ"

if __name__ == '__main__':
    main()