class Solution:
    
    def sub(self, phase):
        
        if phase == self.n:
            self.make_solution()
            return
        
        for i in xrange(self.n):
            
            if self.mask1[i] or self.mask2[phase + i] or self.mask3[self.n + i - phase]:
                continue
                
            self.pick[phase] = i
            self.mask1[i] = True
            self.mask2[phase + i] = True
            self.mask3[self.n + i-phase] = True
            self.sub(phase + 1)
            self.mask1[i] = False
            self.mask2[phase + i] = False
            self.mask3[self.n + i-phase] = False
            
    def make_solution(self):
        r = []
        for i in range(self.n):
            r.append('.'* (self.pick[i]) + 'Q' + '.' * (self.n - self.pick[i] -1))
            
        self.result.append(r)
    
    # @return a list of lists of string
    def solveNQueens(self, n):
        
        self.mask1 = [False  for i in range(n)]
        self.mask2 = [False  for i in range(n*2)]
        self.mask3 = [False  for i in range(n*2)]
        self.pick = [i  for i in range(n)]
        
        self.n = n
        self.result = []
        self.sub(0)
        
        return self.result
