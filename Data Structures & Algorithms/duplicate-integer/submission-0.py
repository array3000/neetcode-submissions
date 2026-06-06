class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for element in nums:
            if element in mySet:
                return True
            else:
                mySet.add(element)
        return False
            