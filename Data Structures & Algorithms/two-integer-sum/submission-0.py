class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_number={} 
        for i in range(len(nums)): 
            num=nums[i] 
            required_number=target-num 
            if required_number in seen_number: 
                return [seen_number[required_number],i] 
            seen_number[num]=i
        
        