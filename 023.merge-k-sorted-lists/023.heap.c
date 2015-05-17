/*
struct ListNode{
    int val;
    struct ListNode *next;
};
*/

void heapAdjustDown(struct ListNode** heap, int* heapSize, int eleIndex){
    int pick = eleIndex;
    int changed;
    int size = *heapSize;
    while(1){
        int up = pick;
        int left = pick * 2 + 2 - 1;
        int right = left + 1;
        changed = 0;
        
        if (left< size && heap[pick]->val > heap[left]->val){
            pick = left;
            changed = 1;
        }
        if (right < size && heap[pick]->val > heap[right]->val){
            pick = right;
            changed = 1;
        }
        if (!changed){
            break;
        }
        struct ListNode* t = heap[up];
        heap[up] = heap[pick];
        heap[pick] = t;
    }
}

void heapAdjustUp(struct ListNode** heap, int* heapSize, int eleIndex){
    int pick = eleIndex;
    int changed=0;
    int size = *heapSize;
    while(1){
        if (pick==0) break;
        int up = (pick+1)/2 - 1;
        changed = 0;

        if (heap[up]->val > heap[pick]->val){
            changed = 1;
        }
        if (!changed){
            break;
        }
        struct ListNode* t = heap[up];
        heap[up] = heap[pick];
        heap[pick] = t;
        pick = up;
    }
}


void heapAdd(struct ListNode** heap, int* heapSize, struct ListNode* ele){
    heap[*heapSize] = ele;
    *heapSize += 1;
    heapAdjustUp(heap, heapSize, *heapSize - 1);
}
 
struct ListNode* heapPop(struct ListNode** heap, int* heapSize){
    if(*heapSize ==0) return 0;
    struct ListNode* r = heap[0];
    heap[0] = heap[*heapSize -1];
    heapAdjustDown(heap, heapSize, 0);
    *heapSize -= 1;
    return r;
}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    
    struct ListNode result;
    result.next = 0;
    struct ListNode* last=&result;
    int i;
    struct ListNode* minNode = 0;

    struct ListNode** heap = malloc(listsSize * sizeof(struct ListNode*));
    int heapSize = 0;

    for(i=0;i<listsSize;i++){
        if (lists[i]){
            heapAdd(heap, &heapSize, lists[i]);
        }
    }
    
    while(1){
        minNode = heapPop(heap, &heapSize);
        if (minNode){
            struct ListNode* next = minNode->next;
            last->next = minNode;
            last = minNode;
            minNode->next = 0;
            if(next){
                heapAdd(heap, &heapSize, next);
            }
        }else{
            break;
        }
    }
    return result.next;
}