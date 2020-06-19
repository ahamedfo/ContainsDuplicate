class Solution(object):
    def containsDuplicate(self, nums):
        dup = {}
        if len(nums) <= 1:
            return False
        for i in nums:
            if i not in dup:
                dup[i] = i
            else:
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
