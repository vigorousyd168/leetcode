# Binary Search
# input: A - a sorted list, key
# output v1: the first element in A that is greater or equal to key
# output v2: the index of the first element in A that is greater or equal to key
# output v3: the index of the first element in A that is equal to key, or -1 if not found

class Solution(object):
	def binSearch1(self, A, key):
		# trivial case
		if len(A) <= 2:
			if A[-1] < key:
				return None # all < key
			for k in range (len(A)-1, 0, -1): # last k is 1 not 0
				if A[k-1] < key:
					return A[k]
			return A[0] # all > key
		p = len(A)/2 # index, not count
		# length 1 -> p = 0, 1 ele in left
		# length 2 -> p = 1, 2 ele in left
		# length 3 -> p = 1, 2 ele in left
		if A[p] < key:
			if p+1 > len(A)-1:
				return None
			return self.binSearch1(A[p+1:], key)
		else:
			return self.binSearch1(A[:p+1], key)
		# need to deal with the case where two elements in A and A[1] >= key
		# see the trivial case solution

# Test case
def main():
    sol = Solution()
    print sol.binSearch1([3,6], 0)

if __name__ == '__main__':
    main()
