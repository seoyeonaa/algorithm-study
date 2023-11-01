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
