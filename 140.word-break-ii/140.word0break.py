class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        
        n = len(s)
        space = {}
        space[n] = []
        
        def search(phase):
            result_list = space.get(phase)
            if result_list is None:
                space[phase] = []
                result_list = space[phase]
        
            for word in wordDict:
                
                j = phase+len(word)
                
                if s.find(word, phase, j) >= 0:
                    if j == n:
                        result_list.append(word)
                        continue

                    if j > n:
                        continue

                    next_result_list = space.get(j)
                    
                    if next_result_list is None:
                        search(j)
                        next_result_list = space[j]
                        
                    result_list.extend("%s %s"%(word, result) for result in next_result_list)
                    
            return space[phase]

        search(0)
        return space[0]