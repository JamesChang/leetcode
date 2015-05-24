class Solution:
    
    def divide(self, i):
                
        if i == self.n:
            self.result.append(self.picks[:])
            return 
            
        element = self.nums[i]
        self.picks.append(element)
        self.divide(i+1)
        self.picks.pop()
        self.divide(i+1)
        return
        
    
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        
        self.n = len(nums)
        self.picks = []
        self.nums = nums
        self.nums.sort()
        self.result = []
        
        self.divide(0)
        return self.result
        
