/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = 0;
    struct ListNode* next = 0;
    while(head){
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}