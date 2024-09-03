import java.util.* ;
import java.io.*; 
public class Solution {
    public static boolean isMatrixSymmetric(int[][] matrix) {
        // Write your code here.

        for(int i = 0; i<matrix.length; i ++) {
            for(int j = i+1; j < matrix.length; j ++) {
                if(matrix[i][j] != matrix[j][i]) {
                    return false;
                }
            }
        }
        return true;
    }
}
