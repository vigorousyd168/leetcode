# 423 Reconstruct Original Digits
class Solution(object):
    t = {}
    count = [0] * 10
    def solve(self, number, letter, word):
        self.count[number] = self.t[letter] if letter in self.t.keys() else 0
        if self.count[number]:
            for c in word:
                self.t[c] = self.t[c] - self.count[number]
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        for c in s:
            if c not in self.t.keys():
                self.t[c] = 1
            else:
                self.t[c] = self.t[c] + 1
        # z -- 0
        self.solve(0, "z", "zero")
        # w -- 2
        self.solve(2, "w", "two")
        # g -- 8 then h -- 3
        self.solve(8, "g", "eight")
        self.solve(3, "h", "three")
        # x -- 6 then s -- 7
        self.solve(6, "x", "six")
        self.solve(7, "s", "seven")
        # u -- 4 then f -- 5
        self.solve(4, "u", "four")
        self.solve(5, "f", "five")
        # i -- 9 then o -- 1
        self.solve(9, "i", "nine")
        self.solve(1, "o", "one")

        res = ""
        for i in range(10):
            res += str(i) * self.count[i]
        return res
def main():
    sol = Solution()
    print sol.originalDigits("owoztneoer") # "012"
    print sol.originalDigits("fviefuro") # "45"
if __name__ == '__main__':
    main()