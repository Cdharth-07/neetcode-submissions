class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        buffer_mem = set()

        for num in nums:
            if num in buffer_mem:
                return True

            buffer_mem.add(num)

        return False