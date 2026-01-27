from typing import List

a = [3, 2, 4, 3]


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    思路: for迴圈用減法找目標 target-i
    限制: 相同元素不可出現2次
    """
    for target1 in nums:
        target2 = target - target1
        target_list = [i for i, v in enumerate(nums) if v == (target2)]
        for k in target_list:
            if nums.index(target1) != k:
                return [nums.index(target1), k]
    return []

print(twoSum(a, 6))
