class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter={} 
        for ele in nums: 
            if ele in counter : 
                counter[ele]+=1 
            else: 
                counter[ele]=1 
        for key in counter: 
            if counter[key]>(len(nums)/2): 
                break 
        return key
        