import sys

# 6. 주식을 사고팔기 가장 좋은 시점
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
# ex) 1일 때 사서 6일 때 팔면 5의 이익을 얻는다
prices = [7, 1, 5, 3, 6, 4]


# 나의 풀이
# enumerate로 인덱스랑 값 얻고, 시간성을 띄는 리스트이기에 자신보다 늦은 순서를 비교하고자 for문 돌려서 찾기?
def maxProfit(prices: list[int]) -> int:
    profit = []

    for i, j in enumerate(prices):  # j가 겹치게 되어 가독성이 떨어짐
        for j in range(i + 1, len(prices)):
            profit.append(prices[j] - prices[i])

    return max(profit)


maxProfit(prices)


# A-1) 브루트 포스로 계산
def maxProfit_mk2(prices: list[int]) -> int:
    max_price = 0  # 0으로 두고 계속 갱신하는 방식, 리스트를 쓰지 않아 용량이 줄어듬

    for i, price in enumerate(prices):  # i = index, prices의 원소를 price라고 둠
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)  # 여기서 가독성이 좋아짐

    return max_price


maxProfit_mk2(prices)


# A-2) 저점과 현재 값과이 차이 계산
def maxProfit_mk3(prices: list[int]) -> int:
    profit = 0
    min_price = sys.maxsize  # min값을 갱신하기 위해 최대 정수값으로 설정

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


# page 198
"""
최대값과 최소값의 초기값을 지정하는 방법에는 여러 가지가 있다.
최대값에는 가장 낮은 값을 초기값으로 해야 어떤 값이든 최대값으로 교체될 수 있고
반대로 최소값에는 가장 높은 값을 초기값으로 해야 어떤 값이든 최소값으로 바로 교체될 수 있다.

max = -sys.maxsize
min = sys.maxsize

float()을 이용하여 다음과 같이 무한대 값을 지정하는 방법도 있다.

max = float('-inf')
min = float('inf')

하지만 다음과 같이 하는 경우 문제가 생길 수 있다.
mn = 999999

파이썬의 숫자형은 임의 정밀도를 지원하며 사실상 무한대의 값을 지정할 수 있다. 
다만 아무리 큰 수라 할지라도 얼마든지 더 큰수가 지정될 수 있다.

사실 sys.maxsize으로 선언하는 것도 파이썬에서는 큰 의미가 없다.
하지만 일반적인 코딩 테스트의 경우, 모든 언어에 대응하는 공통된 테스트 케이스로 구성되어 있어
파이썬에서 sys.maxsize로 처리하는 정도만으로 충분히 모든 테스트 케이스를 통과할 수 있다.
"""
