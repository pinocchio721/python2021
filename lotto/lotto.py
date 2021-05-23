import random
# # # 1. Lotto 번호 생성하기
# # lotto_list = random.sample(range(1,46), 6)
# # print(lotto_list)

# # 3. Lotto 여러 개 생성하기
# print("로또 번호 생성기")
# print("게임 수를 입력하세요")
# game_number = int(input("게임 수: "))
# for i in range(game_number):
# #     lotto_list = random.sample(range(1,46), 6)
# #     lotto_list.sort()
# #     print(lotto_list)
# # print("생성 완료")

# # 숫자만 입력 받기
# print("로또 번호 생성기")
# print("게임 수를 입력하세요")
# while True:
#     game_number = input("게임 수: ")
#     if game_number.isdigit():
#         for i in range(int(game_number)):
#             lotto_list = random.sample(range(1,46), 6)
#             lotto_list.sort()
#             print(lotto_list)
#         print("생성 완료")
#         break
#     else:
#         print("다시 입력하세요")

# 5. 로또 API 사용하기
import requests
from pprint import pprint
drwNo = 900
url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={drwNo}'
res = requests.get(url).json()
# pprint(res)
prize_list = []
prize_list.append(res['drwtNo1'])
prize_list.append(res['drwtNo2'])
prize_list.append(res['drwtNo3'])
prize_list.append(res['drwtNo4'])
prize_list.append(res['drwtNo5'])
prize_list.append(res['drwtNo6'])
print(prize_list)

lotto_list = random.sample(range(1,46), 6)
lotto_list.sort()
print(lotto_list)
count = 0
for i in prize_list:
    if i in lotto_list:
        count += 1
print(count)
if count == 3:
    print("5등")
elif count == 4:
    print("4등")
elif count == 5:
    print("3등")
elif count == 6:
    print(f"1등 {res['firstAccumamnt']}원")
else:
    print("다음 기회에")
