class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new_dict = {}
        for i in nums:
            if i in new_dict:
                new_dict[i] += 1
            else:
                new_dict[i] = 1
        
        return max(new_dict, key = new_dict.get)
