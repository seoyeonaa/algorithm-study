import collections
import re

# 6장
# 1. 유효한 팰린드롬 확인하기
# A-1) 리스트로 변환
ex = "A man, a plan, a canal: Panama"


def isPalindrome1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():  # 문자 여부 판단
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


isPalindrome1(ex)  # True


# A-2) 데크 자료형을 이용한 최적화 (FIFO, First In First Out)
def isPalindrome2(s: str) -> bool:
    # 자료형 데크로 선언
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


isPalindrome2(ex)


# A-3) 정규식 활용
def isPalindrome3(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub("[^a-z0-9]", "", s)

    return s == s[::-1]  # 문자열 뒤집기


isPalindrome3(ex)


# 2. 문자열 뒤집기

# Q) 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴없이 리스트 내부를 직접 조작하라.
# A-1) 투 포인터를 이용한 스왑
ex = ["h", "e", "l", "l", "o"]
ans = ["o", "l", "l", "e", "h"]


def reverseString1(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


reverseString1(ex)
ex == ans


# A-2) 파이썬다운 방식


def reverseString2(s: list[str]) -> None:
    s.reverse()


reverseString2(ex)
ex == ans


# 3.로그 파일 재정렬
# Q) 로그를 재정렬하라. 기준은 다음과 같다.
# 1) 로그의 가장 앞 부분은 식별자이다.
# 2) 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3) 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4) 숫자 로그는 입력 순서대로 한다.

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


# A) 람다와 + 연산자를 사용
def reorderLogFiles(logs: list[str]) -> list:
    letters = []
    digits = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(
        key=lambda x: (x.split()[1:], x.split()[0])
    )  # 식별자는 순서에 영향을 끼치지 않음 [1:], 하지만 같으면 식별자 순 [0]
    return letters + digits


reorderLogFiles(logs)


# 4. 가장 흔한 단어
# Q) 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 기준은 다음과 같다.
# 1) 대소문자를 구분하지 않는다.
# 2) 구두점(마침표, 쉼표 등) 또한 무시한다.
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# A-1) 리스트 컴프리헨션, Counter 객체 사용


def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [
        word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned
    ]

    counts = collections.Counter(words)
    # 가장 흔한 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]


mostCommonWord(paragraph, banned)
