class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list=2*nums 
        lenght_list=len(nums)  
        for i in range(lenght_list): 
            new_list[i]=nums[i]
            new_list[i+lenght_list]=nums[i]
        return new_list
        