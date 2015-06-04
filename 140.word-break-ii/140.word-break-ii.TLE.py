class Solution:
    
    def match_word(self, s, index, word):
        
        n = len(word)
        i=0
        
        while(index-i >=0 and n-i -1>=0 and s[index-i] == word[n-i-1]):
            i+=1
        
        return i == n
        
    
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        
        n = len(s)
        results = {}
        
        for i in range(n):
            for word in wordDict:
                if self.match_word(s, i, word):
                    #print "match", i, word
                    result_list = results.setdefault(i, [])
                    
                    if i - len(word) == -1:
                        result_list.append(word)
                                            
                    last_word_list = results.get(i - len(word), [])
                    result_list.extend("%s %s" % (last_word, word) for last_word in last_word_list)
                    
                    
        return results.get(n-1, [])


Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
