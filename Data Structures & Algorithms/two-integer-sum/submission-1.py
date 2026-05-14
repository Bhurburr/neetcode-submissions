class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            nums1 = nums[i]
            for j in range(len(nums)):
                nums2 = nums[j]
                if nums1 + nums2 == target and j != i:
                    num_list = [i, j]
                    num_list.sort()
                    return num_list