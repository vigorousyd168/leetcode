    public int partitionDisjoint(int[] A) {
        int n = A.length;
        int[] rightMin = new int[n];
        rightMin[n-1] = A[n-1];
        for (int i = n-2; i >= 0; i--) {
            rightMin[i] = Math.min (rightMin[i+1], A[i]);
        }
        int leftMax = -1;
        for (int i = 0; i < n-1; i++) {
            leftMax = Math.max (leftMax, A[i]);
            if (leftMax <= rightMin[i+1])
                return i+1;
        }
        return -1;
    }