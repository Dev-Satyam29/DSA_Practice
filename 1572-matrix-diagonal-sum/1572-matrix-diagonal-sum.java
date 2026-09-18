class Solution {
    public int diagonalSum(int[][] mat) {
        int row=mat.length;
        int total=0;
        for(int i=0;i<row;i++){
            total=total+mat[i][i];
            total=total+mat[i][row-i-1];
        }
        if(row%2!=0)
        total=total-mat[row/2][row/2];
        return total;
    }
    
}