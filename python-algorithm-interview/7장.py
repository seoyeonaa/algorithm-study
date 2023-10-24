# 7장
# 1. 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

nums = [2, 7, 11, 15]
target = 18


# A-1) 브루트 포스로 계산


def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


twoSum(nums, target)


# A-2) in을 이용한 탐색


def twoSum_mk2(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1 :]:
            return [nums.index(n), nums[i + 1 :].index(complement) + (i + 1)]


twoSum_mk2(nums, target)


# A-3) 첫 번째 수를 뺀 결과 키 조회


def twoSum_mk3(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if (target - num) in nums and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

    return []


twoSum_mk3(nums, target)


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


# A-2) 스택 쌓기

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap(height: list[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and (height[i] > height[stack[-1]]):
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            print(f"{i}번째 distance :", distance)

            waters = min(height[i], height[stack[-1]]) - height[top]
            print(f"{i}번째 water :", waters)

            volume += distance * waters
            print(f"{i}번째 volume :", volume)

        stack.append(i)
        print(f"{i}번째 stack :", stack)

    return volume


trap(height)


# 3. 세 수의 합
# A-1) 브루트 포스로 계산

nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    print(i, j, k)

    return results


threeSum(nums)


# A-2) 투 포인터 합 계산

nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀나가며 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵처리
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

        return results


# 4. 배열 파티션
# n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

nums = [1, 4, 2, 3]


# A-1) 오름차순 풀이


def arrayPairSum(nums: list[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


arrayPairSum(nums)


# A-2) 짝수 번째 값 계산


def arrayPairSum_mk2(nums: list[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


arrayPairSum_mk2(nums)


# A-3) 파이썬다운 방식


def arrayPairSum(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])


# 5. 자신을 제외한 배열의 곱
# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈 (나눗셈 X)

nums = [1, 2, 3, 4]


def productExceptSelf(nums: list[int]) -> list[int]:
    out = []
    p = 1
    # 왼쪽 곰셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out


productExceptSelf(nums)
