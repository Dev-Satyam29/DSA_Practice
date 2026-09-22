class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int row = mat.length;
        int col = mat[0].length;
        int[] ans = new int[row * col];
        int r = 0;
        int c = 0;
        for (int k = 0; k < row * col; k++) {
            ans[k] = mat[r][c];
            if ((r + c) % 2 == 0) {
                if (c == col - 1) {
                    r++;
                }
                else if (r == 0) {
                    c++;
                }
                else {
                    r--;
                    c++;
                }
            }
            else {

                if (r == row - 1) {
                    c++;
                }
                else if (c == 0) {
                    r++;
                }
                else {
                    r++;
                    c--;
                }
            }
        }
        return ans;
    }
}