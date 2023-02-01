#include <stdio.h>

void init(double *mat, int row, int col) {
    int i, j;
//    for (i = 0; i < row * col; i++) {
//        *(mat + i) = i;
//    }
    for(i = 0; i < row; i++) {
        for(j = 0; j < col; j++) {
            *(mat + (i * col + j)) = i + j + 2;
        }
    }
}