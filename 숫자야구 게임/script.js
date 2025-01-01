// TODO 1 : input 태그에 0~9까지의 숫자 넣기(시간이 된다면 그 안의 숫자가 들어가지 않으면 잘못입력되었다는 예외 처리 필요)
// input 태그와 연결
let userInput1 = document.getElementById("number1").value;
let userInput2 = document.getElementById("number2").value;
let userInput3 = document.getElementById("number3").value;

// user의 input을 결과와 비교하는 버튼
const submitButton = document.getElementsByClassName("submit-button");

// span 태그인 남은 횟수 연결
const attempts = document.getElementById("attempts");

// user의 input과 random 난수를 비교해 출력되는 div 박스
const results = document.getElementById("results");

// 결과가 출력되는 results의 div 박스의 부모 div
const checkResult = document.getElementsByClassName("check-result");

// 결과가 맞았는지 틀렸는지 Success or Fail이 출력되는 img div
const resultImg = document.getElementById("game-result-img");

// random한 값 3개를 저장할 변수
let answer = [];
let ball = 0;
let strike = 0;

// 초기 attempts 값으로 9를 지정
// TODO 2: 남은 시도 횟수는 9로 설정!!
attempts.innerHTML = 9;
let remainingAttepts = 9;

// 게임 초기화
game_setting();

// 본격적으로 필요한 로직들 작성!
function check_numbers() {
    // TODO 5: 입력되지 않은 input이 있다면 숫자를 확인하지 않고 input 창만 비움
    // attemp는 줄어들지 않고 input 창만 비우기
    // -> if 문으로 구현
    userInput1 = document.getElementById("number1").value;
    userInput2 = document.getElementById("number2").value;
    userInput3 = document.getElementById("number3").value;
    const userInputs = [userInput1, userInput2, userInput3];

    console.log(userInputs);

    if (userInputs.includes('')){
        userinput_clear();
        return
    }

    else {
        compare_number(userInputs);
        append_result(userInputs);
        userinput_clear();
    }
    return userInputs;
}

// TODO 3: 중복되지 않는 3개의 0 ~ 9까지의 숫자 랜덤으로 생성
function game_setting() {
    const numbers = [];

    while (numbers.length < 3){
        const randomNumber = Math.floor(Math.random()*10).toString();
        if (!numbers.includes(randomNumber)){
            numbers.push(randomNumber);
        }
    }

    answer = numbers;

    console.log(answer);
}

function compare_number(userInputs) {
    // TODO 6-1: 입력된 숫자들과 정답을 비교하여 결과를 생성하는 로직 만들기
    for (let i = 0; i < 3; i++){
        for (let j = 0; j < 3; j++){
            if (userInputs[i] === answer[j]){
                ball++;
            }
        }
        if (userInputs[i] === answer[i]){
            strike++;
            ball--;
        }
    }

    console.log(strike);
    console.log(ball);

    // TODO 2: 시도할 때마다 남은 시도 횟수 1씩 감소
    remainingAttepts--;
    attempts.innerHTML = remainingAttepts;

    console.log(attempts);
}

// TODO 4: html의 input과 결과창의 내용을 비움
function userinput_clear() {
    // input 값 초기화
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";

    // number1 input으로 focus 이동
    document.getElementById("number1").focus();
}

// TODO 6: 숫자 3개가 입력되었다면 결과 확인
    // 2. 생성된 결과에 따라 html 업데이트하기
    // 3. 게임이 끝났는지 체크하고 결과에 따라 이미지를 출력합니다. 게임이 끝나면 **확인하기** 버튼은 비활성화합니다.
    //     - 이미지는 id가 `game-result-img`  img 태그를 사용합니다.
    //     - 승리 시 `success.png` , 패배 시 `fail.png` 를 출력합니다.

// result에 div 추가
function append_result(userInputs) {
    let result1 = document.createElement("div");
    result1.classList.add("result", "left");
    result1.style.width = "40%";
    result1.style.height = "40px";
    result1.style.backgroundColor = "white"; // 첫 번째 결과 스타일
    result1.style.lineHeight = "40px";
    result1.innerText = userInputs.join(" "); // 입력값 표시
    checkResult[0].appendChild(result1); // 좌측 추가

    // ":" 텍스트 추가
    const colonText = document.createElement("div");
    colonText.style.width = "30%";
    colonText.style.height = "40px";
    colonText.style.backgroundColor = "yellow";
    colonText.style.textAlign = "center";
    colonText.style.lineHeight = "40px";
    colonText.innerText = ":"; // 텍스트 추가
    checkResult[0].appendChild(colonText); // 가운데 추가

    const result2 = document.createElement("div");
    result2.classList.add("result", "right");
    result2.style.width = "40%";
    result2.style.height = "40px";
    result2.style.display = "flex";
    result2.style.flexDirection = "row";
    result2.style.justifyContent = "flex-end";
    result2.style.alignItems = "center";
    result2.style.backgroundColor = "aqua"; // 두 번째 결과 스타일
    checkResult[0].appendChild(result2); // 우측 추가

    // 우측에 S, B 표시
    // right에 S, B 갯수 표시
    // S와 B가 모두 0이라면 O 출력

    if (strike === 0 && ball === 0) {
        const rightContainer = document.getElementsByClassName("right");

        const outContainer = document.createElement("div");
        outContainer.classList.add("num-result", "out");
        outContainer.innerText = "O";
        outContainer.style.boxSizing = "border-box";
        rightContainer[0].appendChild(outContainer);
    }
    // 아니라면 S와 B의 각각의 갯수 출력
    else {
        // 우측 결과 div에 S, B 갯수 표시
        const rightContainer = document.getElementsByClassName("right");

        const sNumContainer = document.createElement("div");
        sNumContainer.innerText = strike;
        sNumContainer.classList.add("num-result");
        rightContainer[0].appendChild(sNumContainer);

        const strikeContainer = document.createElement("div");
        strikeContainer.classList.add("num-result", "strike");
        strikeContainer.innerText = "S";
        strikeContainer.style.boxSizing = "border-box";
        rightContainer[0].appendChild(strikeContainer);

        const bNumContainer = document.createElement("div");
        bNumContainer.classList.add("num-result");
        bNumContainer.innerText = ball;
        rightContainer[0].appendChild(bNumContainer);

        const ballContainer = document.createElement("div");
        ballContainer.classList.add("num-result", "ball");
        ballContainer.style.boxSizing = "border-box";
        ballContainer.innerText = "B";
        rightContainer[0].appendChild(ballContainer);
    }
}