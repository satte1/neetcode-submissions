class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_checker={}
        for i in range(len(strs)): 
            key="".join(sorted(strs[i]))
            if key in anagram_checker:
                anagram_checker[key].append(strs[i]) 
            else: 
                anagram_checker[key]=[strs[i]] 
        return list(anagram_checker.values())

        