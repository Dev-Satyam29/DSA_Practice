class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int element=matrix[0][0];
        int row=matrix.length;
        int col=matrix[0].length;
        for(int i=1;i<row;i++){
            for(int j=1;j<col;j++){
                if(matrix[i][j]!=matrix[i-1][j-1]){
                    return false;
                    }
            }
        }
        return true;
    }
}