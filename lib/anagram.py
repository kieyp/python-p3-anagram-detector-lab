# your code goes here

class Anagram:
    
    def __init__(self,word):
        
        self.word=word.lower()
        
        
    def match(self,data):
        
        return [n for n in data if  self.is_match(n)]
    
    
    def is_match(self,candidate):
        
        candidate=candidate.lower()
        
        return sorted(self.word) == sorted(candidate)
    

listen=Anagram("Boniface")

result=listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)