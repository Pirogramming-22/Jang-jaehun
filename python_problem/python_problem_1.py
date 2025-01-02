# TODO 1: 변수 num을 0으로 선언
num = 0

# TODO 3-1: 2단계에서 정수를 입력하지 않는 경우, `정수를 입력하세요`를 출력한다.
# TODO 3-2: 2단계에서 1,2,3을 입력하지 않는 경우, `1,2,3 중 하나를 입력하세요`를 출력한다.
# TODO 3-3: 올바른 값이 입력될 때까지 입력을 요구한다.
while True:
    try:
        # TODO 2: input() 함수를 이용하여 1에서 3사이의 정수를 입력받는 코드를 작성하여라.
        user = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
    except ValueError:
        print("정수를 입력하세요")
    else:
        if not (1 <= user <= 3):
            print("1, 2, 3 중 하나를 입력하세요")
        else:
            break