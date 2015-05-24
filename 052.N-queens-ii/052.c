
int divide(int n, int col, int l, int r) {
    int result = 0;
    int mask = (1 << n) - 1;
    if (col == mask) {
        return 1;
    } else {
        int valid = mask & (~(col | l | r));
        while (valid) {
            int p = valid & (~valid + 1);
            valid -= p;
            result += divide(n, col + p, (l + p) << 1, (r + p) >> 1);
        }
    }
    return result;
}

int totalNQueens(int n) {
    return divide(n, 0, 0, 0);
}