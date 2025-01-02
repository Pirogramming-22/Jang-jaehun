# TODO 1: 변수 num을 0으로 선언
num = 0
player = "A"

# TODO 3-1: 2단계에서 정수를 입력하지 않는 경우, `정수를 입력하세요`를 출력한다.
# TODO 3-2: 2단계에서 1,2,3을 입력하지 않는 경우, `1,2,3 중 하나를 입력하세요`를 출력한다.
# TODO 3-3: 올바른 값이 입력될 때까지 입력을 요구한다.
def user_input(num):
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
    return user

# TODO 4: 변수 num 을 이용하여, 2단계에서 입력한 수만큼 숫자를 출력하는 코드를 작성하여라.
""" 
TODO 5:
- 1에서 3사이의 정수를 입력받는 코드를 작성하여라.
    
     `부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :`
    
- 정수를 입력하지 않는 경우, `정수를 입력하세요`를 출력한다.
- 1,2,3을 입력하지 않는 경우, `1,2,3 중 하나를 입력하세요`를 출력한다.
- 올바른 값이 입력될 때까지 입력을 요구한다.
- 변수 `num`을 이용하여 입력한 수만큼 숫자를 출력하는 코드를 작성하여라.
"""

# TODO 8: 6단계까지 중복되는 코드를 찾아 함수로 만들어라. 이때, 함수 이름은 brGame으로 한다.
def brGame():
    global player
    if (player == "A"):
        player = "B"
    else:
        player = "A"

def player_print(player, i):
    print(f"player{player} : {i + 1}")

# TODO 6: 배스킨라빈스31 게임은 참여자가 번갈아가며 숫자를 부른다. 게임이 끝날 때까지 playerA와 playerB에게 번갈아가며 부를 숫자의 개수를 입력받는 코드를 작성하여라.
def check_num(num, user, player):
    for i in range(num, num + user): # user가 입력한 수만큼 반복
        # TODO 6-1: 값에 31이 포함되어있는지 확인(포함되어있다면 해당 플레이어와 num 리턴)
        if i == 30:
            player_print(player, i)
            num += user
            return num
        player_print(player, i)
    # if (player == "A"):
    #     player = "B"
    # else:
    #     player = "A"
    brGame()
    # num 값 업데이트
    num += user
    return num

# main code
while True:
    # default user
    user = user_input(num)
    # num, player = check_num(num, user, player)
    num = check_num(num, user, player)
    # ### 디버깅 코드
    # print(f"final_num : {num}")
    if num >= 31:
        # TODO 7: 게임이 끝났을 때, 누가 이겼는지 화면에 출력하여라.
        # if (player == "A"):
        #     player = "B"
        # else:
        #     player = "A"
        brGame()
        print(f"player{player} win")
        break