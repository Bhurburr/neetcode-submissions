class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) # removing this line makes it slower?
        new_list = []
        for _ in range(2):
            for j in range(len(nums)):
                new_list.append(nums[j])
        return new_list