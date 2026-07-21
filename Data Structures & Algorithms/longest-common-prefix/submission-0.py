class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]  # pehle word ko prefix maan lo
        
        for i in range(1, len(strs)):  # baaki sabse compare karo
            next_element = strs[i]
            j = 0
            while j < len(prefix) and j < len(next_element):
                if prefix[j] != next_element[j]:
                    break
                j += 1
            prefix = prefix[:j]  # prefix ko trim karte jao
            
            if prefix == "":  # early exit
                return ""
        
        return prefix
        