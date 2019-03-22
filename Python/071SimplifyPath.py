# 071 Simplify Path
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = []
        if len(path) < 2:
            return path
        up = 0
        temp = ''
        for i in xrange(len(path)-1, -1, -1):
            if path[i] == '/':
                if temp == '.' or temp == '':
                    temp = ''
                    continue
                elif temp == '..':
                    up += 1
                elif up > 0:
                    up -= 1
                else:
                    s = [temp] + s
                temp = ''
            else:    
                temp = path[i] + temp
        return '/' + '/'.join(s)

def main():
    sol = Solution()
    print sol.simplifyPath("/home/") # "/home"
    print sol.simplifyPath("/a/./b/../../c/") # "/c"
    print sol.simplifyPath("/abc/...") # "/abc/..."
if __name__ == '__main__':
    main()