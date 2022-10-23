class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}
        index_table = {}
        index_list = []

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in hash_table:
                index_list.append([index_table[diff], i])
            else:
                hash_table[nums[i]] = nums[i]
                index_table[nums[i]] = i

        return index_list[0]