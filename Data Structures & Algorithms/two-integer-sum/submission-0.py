class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # do you need to define the key and value for this hashmap? (yeah cuz its a dictionary)
        cachedNums = {} #number : index

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cachedNums:
                return [cachedNums[diff], i]
            # else cache this value
            # cachedNums.append(nums[i], i) WRONG WAY OF USING DICT
            cachedNums[nums[i]] = i


        