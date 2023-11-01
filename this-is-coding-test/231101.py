# page 86; Greedy Algorithm
# 거스름돈 1260원을 동전으로 줄 시 거슬러 주는 횟수는?
changes = 1260
coins = [500, 100, 50, 10]


# 나의 풀이
def givechanges(changes, coins):
    print(f"거슬러 줘야 할 돈은 {n}원 입니다.")
    count = 0  # 횟수 0부터 시작
    while changes > 0:  # 거스름돈이 0보다 클 때 까지
        if changes // max(coins) >= 1:  # 한 번이라도 거슬러 줄 수 있는지?
            print(f"{max(coins)}을 거슬러 줍니다.")
            changes -= max(coins)
            count += 1

        else:  # 해당 단위의 동전으로 못 거슬러 준다면?
            coins.remove(max(coins))

    return f"총 {count}번 거슬러 주었습니다."


# 답안
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
