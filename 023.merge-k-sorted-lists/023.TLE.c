/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    
    struct ListNode result;
    result.next = 0;
    struct ListNode* last=&result;
    int i;
    struct ListNode* minNode = 0;
    
    while(1){
        
        minNode = 0;
        int pick = 0;
        for(i=0;i<listsSize;i++){
            if (lists[i] != 0 && (minNode==0 || lists[i]->val < minNode->val)){
                minNode = lists[i];
                pick = i;
            }
        }
        
        if (minNode == 0){
            break;
        }else{
            lists[pick] = minNode->next;
            minNode->next = 0;
            last->next = minNode;
            last = minNode;
        }
        
    }
    return result.next;
}