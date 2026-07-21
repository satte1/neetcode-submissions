class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #checking lenght of words 
        if len(s)!=len(t): 
            return False  
        #creatting hashmap for for tally 
        tally_letter={} 
        for chr in s:
            if chr in tally_letter: 
                tally_letter[chr]+=1 
            else: 
                tally_letter[chr]=1 
        #now checking charater in t 
        for chr in t:
            if (chr  not in tally_letter) or (tally_letter[chr]==0):
                return False
            tally_letter[chr]-=1 
        return True
