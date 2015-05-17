int lengthOfLongestSubstring(char* s) {
    
    boolean mark[255];
    char* index[255];
    
    char* i = s;
    char* j = s;
    result = *j>0 ? 1:0;
    
    while(*j){
        int c = ord(*j)
        if (!mark[c]){
            mark[c]=true;
            index[c] = j;
            j=j+1;
            int width = j-i;
            if (width>result){
                result = width;
            }
        }else{
            for(;i<=index[c];i++){
                mark[ord(*i)]=false;
            }
            mark[c] = true;
            index[c] = j;
            j=j+1;
        }
    }
}