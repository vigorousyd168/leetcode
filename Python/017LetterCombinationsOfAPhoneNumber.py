# 017 Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def helper(prefix, digits):
            res = []
            if len(digits) == 0:
                return [prefix]
            else:
                c = digits[0]
                for l in d[c]:
                    res += helper(prefix+l, digits[1:])
            return res
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if len(digits) == 0:
            return []
        return helper("", digits)
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        return reduce(lambda acc, digit: [x+y for x in acc for y in d[digit]], digits, [""])
def main():
    sol = Solution()
    print sol.letterCombinations("23") # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print sol.letterCombinations("2") # ["a", "b", "c"]
    print sol.letterCombinations("") # []
if __name__ == '__main__':
    main()