# leetcode 42
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
# leetcode 15
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
