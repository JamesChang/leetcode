
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define true 1
#define false 0
#define bool int

bool _exist(char** board, int boardRowSize, int boardColSize, char* word, int row, int col, char* mask) {
    printf("test %d %d %c\n", row, col, *word);
    if (row >= boardRowSize || row<0) return false;
    if (col >= boardColSize || col<0) return false;
    if (mask[row * boardColSize + col]) return false;
    printf("%d %d %c\n", row, col, board[row][col]);
    if (board[row][col] != *word) return false;

    
    if (*(word +1) == 0) return true;
    
    mask[row*boardColSize + col] = 1;
    int r = 0;
    r = _exist(board, boardRowSize, boardColSize, word+1, row-1, col, mask);
    if (r ) return r;
    r = _exist(board, boardRowSize, boardColSize, word+1, row, col+1, mask);
    if (r ) return r;
    r = _exist(board, boardRowSize, boardColSize, word+1, row+1, col, mask);
    if (r ) return r;
    r = _exist(board, boardRowSize, boardColSize, word+1, row, col-1, mask);
    if (r ) return r;
    
    mask[row*boardColSize + col] = 0;
    return r;
}

bool exist(char** board, int boardRowSize, int boardColSize, char* word) {
    
    char* mask = (char*) malloc(boardRowSize*boardColSize);
    memset(mask, 0, sizeof(mask));
    
    for(int i=0;i<boardRowSize;i++)
    {
        for(int j=0;j<boardColSize;j++)
        {
            
            if (_exist(board, boardRowSize, boardColSize, word, i, j, mask))
            {
                return true;
            }
            
        }
    }
    return false;
}

void main(){
   char* b1 = "ABC";
   char* b2 = "HGD";
   char* b3 = "IFE";

   char* b[3];
   b[0] = b1;
   b[1] = b2;
   b[2] = b3;
    
   int r = exist(b, 3,3,"ABCDEFGHI");
   printf("%d\n", r);

}
