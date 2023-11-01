import collections
import re

# 5. 그룹 애너그램
# Q) 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
ex = ["eat", "tea", "tan", "ate", "nat", "bat"]


def groupAnagram(strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams["".join(sorted(word))].append(word)

    return list(anagrams.values())


groupAnagram(ex)


# 6. 가장 긴 팰린드롬 부분 문자열
# Q) 가장 긴 팰린드롬 부분 문자열을 출력하라.
ex = "babad"


def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1 : right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ""

    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


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

nums = [2, 7, 11, 15]
target = 18


def twoSum_mk3(nums: list[int], target: int) -> list[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if (target - num) in nums and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

    return []


twoSum_mk3(nums, target)
