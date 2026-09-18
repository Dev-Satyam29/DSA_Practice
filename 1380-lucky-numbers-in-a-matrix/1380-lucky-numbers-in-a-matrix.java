import java.util.*;

class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        int rows = matrix.length;
        int cols = matrix[0].length;
        for (int i = 0; i < rows; i++) {
            int rowMin = matrix[i][0];

            for (int j = 1; j < cols; j++) {
                rowMin = Math.min(rowMin, matrix[i][j]);
            }
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == rowMin) {
                    int colMax = matrix[0][j];

                    for (int k = 1; k < rows; k++) {
                        colMax = Math.max(colMax, matrix[k][j]);
                    }

                    if (matrix[i][j] == colMax) {
                        ans.add(matrix[i][j]);
                    }
                }
            }
        }

        return ans;
    }
}