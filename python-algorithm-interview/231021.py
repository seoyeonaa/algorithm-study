# A-4) 조회 구조 개선
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
nums = [2, 7, 11, 15]
target = 18


def twoSum_mk4(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


twoSum_mk4(nums, target)


# A-5) 투 포인터 이용
# 정렬이 되어있어야 하는데 그러면 고유의 인덱스가 사라짐
def twoSum_mk5(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


# 2. 빗물 트레핑
# A-1) 투 포인터를 쵀대로 이동

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap(self, height: list[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1

        else:
            volume += right_max - height[right]
            right -= 1

    return volume
