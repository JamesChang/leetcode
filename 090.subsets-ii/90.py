class Solution:
        
    
    def divide(self, i):
                
        if i == self.n:
            self.result.append(self.picks[:])
            return 
            
        element = self.nums[i]
        j = i
        while j < self.n and self.nums[j] == element:
            j+=1
        
        k = i
        while k < self.n and k<j:
            self.picks.append(element)    
            self.divide(j)
            k += 1
        
        k = i
        while k < self.n and k<j:
            self.picks.pop()
            k += 1
        
        self.divide(j)
        return
        
    
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        
        self.n = len(nums)
        self.picks = []
        self.nums = nums
        self.nums.sort()
        self.result = []
        
        self.divide(0)
        return self.result
        
