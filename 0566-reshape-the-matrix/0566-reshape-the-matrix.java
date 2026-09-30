class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int row=mat.length;
        int col=mat[0].length;
        if(r*c!=row*col){
            return mat;
        }
        int[] arr=new int[row*col];
        int[][] new_mat=new int[r][c];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                arr[i*col+j]=mat[i][j];
            }
        }
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                new_mat[i][j]=arr[i*c+j];
            }
        }
        return new_mat;
    }
}