# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        array = []
        for l in lists:
            while l:
                array.append(l)
                l=l.next
            
        array.sort(key=lambda _:_.val)
        for i in xrange(len(array)-1):
            array[i].next = array[i+1]
        if array:
            array[-1].next = None
            return array[0]
        else:
            return None