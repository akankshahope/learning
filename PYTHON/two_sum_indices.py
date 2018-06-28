############### PROBLEM STATEMENT #############
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [3,2,4], target = 6,

# Because nums[1] + nums[2] = 2 + 4 = 6,
# return [1, 2]

# SOLUTION APPROACH
# Brute Force
# Loop through each element x and find if there is another value that equals to target−x

# COMPLEXITY ANALYSIS

# Time complexity : O(n^2) For each element, we try to find its complement by looping through the rest of array which takes O(n) time. Therefore, the time complexity is O(n^2)
# Space complexity : O(1)


def twoSumIndices(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    finalIndices = []
    for i in range(0, len(nums)):
        item = target - nums[i]
        nums[i] = "executed this"
        if item in nums:
            finalIndices.append(i)
            finalIndices.append(nums.index(item))
            return finalIndices
    return []


print twoSumIndices([3,2,4],6)