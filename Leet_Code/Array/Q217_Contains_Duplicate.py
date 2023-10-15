# Contains Duplicate
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


# 用hash table的方法，时间复杂度O(n)，空间复杂度O(n)
def containsDuplicate(nums):
    """
    Args:
        nums (List[int]): list of integers
    Returns:
        bool: True if any value appears at least twice in the array
    """
    hash_table = {}
    for i in nums:
        if i in hash_table:
            return True
        else:
            hash_table[i] = 1
    return False


# 用set的方法，时间复杂度O(n)，空间复杂度O(n)
def containsDuplicate(nums):
    """
    Args:
        nums (List[int]): list of integers
    Returns:
        bool: True if any value appears at least twice in the array
    """
    return len(nums) != len(set(nums))


# 用sort的方法，时间复杂度O(nlogn)，空间复杂度O(1)
def containsDuplicate(nums):
    """
    Args:
        nums (List[int]): list of integers
    Returns:
        bool: True if any value appears at least twice in the array
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
