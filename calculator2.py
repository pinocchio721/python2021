#2. 직접 간단한 계산기 구현하기
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def rem(a,b):
    return a % b

print("=" * 20)
print("1. 더하기\n2. 빼기\n3. 곱하기\n4. 나누기\n5. 나머지\n6. 끝내기")
print("=" * 20)

while True:
    mode = input("원하는 계산기 기능을 입력해주세요:)")

    if mode.isdigit():
        mode = int(mode)
    else:
        print("다시 입력해주세요:(")
        continue



    if 1 <= mode <= 6:
        if mode == 6:
            e = input("끝내시겠습니까? Y/N")
            if e == "Y":
                print("종료하겠습니다.")
                break
            else:
                continue

        number1 = int(input("첫번째 숫자를 입력해주세요"))
        number2 = int(input("두번째 숫자를 입력해주세요"))
        if mode == 1:
            result = add(number1,number2)
        if mode == 2:
            result = sub(number1,number2)
        if mode == 3:
            result = mul(number1,number2)
        if mode == 4:
            result = div(number1,number2)
        if mode == 5:
            result = rem(number1,number2)


        print(f'결과는 {result}입니다.')
        print('-'*20)

        
    else: 
        print("다시 입력해주세요:(")
