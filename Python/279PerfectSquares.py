# 279 Perfect Squares
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = [0]
        current = []
        visited = [False] * n
        if n <= 0:
            return 0
        count = 0
        while True:
            count += 1
            # now we push all numbers that can be represented as {count} perfect squares
            # and is less than or equal to n
            for base in prev:
                j = 1
                while base + j*j <= n:
                    candidate = base + j*j
                    if candidate == n:
                        return count
                    if candidate > n:
                        break
                    if not visited[candidate]:
                        visited[candidate] = True
                        current.append(candidate)
                    j += 1
            prev = current
            current = []

def main():
    sol = Solution()
    print sol.numSquares(1) # 1
    print sol.numSquares(2) # 2
    print sol.numSquares(7) # 4
    print sol.numSquares(12) # 3
    print sol.numSquares(16) # 1
    print sol.numSquares(20) # 2
    print sol.numSquares(21) # 3
    print sol.numSquares(50000) # 2

if __name__ == '__main__':
    main()