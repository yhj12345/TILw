# 1~45가지의 숫자 중 에 6개만 뽑아서 리스트에 담아서 출력
# random 불러오기
import random
winners = [1,2,3,4,5,6]
# 1~45의 숫자 범위 만들기
# 리스트로 만들기
numbers = list(range(1, 46))

# 비복원추출로 6개 뽑기
# 6개 뽑아서 lotto 변수에 담기를 1000번 반복
for i in range(1000):
    lotto = random.sample(numbers, 6)
    # 당첨 횟수를 기록
    count = 0 
    # print(lotto[0] ~ [5])
    for num in lotto:
        # lotto가 가지고 있는 값든 하나하나가
        # winners안에 들어 있다면....
        if num in winners:
            # 한개 당첨
            count = count + 1
    # 숫자 6개를 다 확인하고 나서
    # 6개 당첨 == 1등 당첨
    if count == 6:
        print(i)
        print('1등!!!!!!')