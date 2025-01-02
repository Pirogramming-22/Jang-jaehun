const recordList = document.querySelector('.record_list');
const recordContainer = document.querySelector('.record_container');
const checkAllButton = document.querySelector('.check_button_all');
const deleteButton = document.querySelector('.delete');

var time = document.getElementsByClassName('time')[0];
var s = 0, ms = 0; // 초, 밀리초
var timer;

// 1. 스톱워치 시작
function start() {
    timer = setInterval(Timer, 10); // 10ms마다 Timer 호출
}

// 2. 스톱워치 정지 및 기록 추가
function stop() {
    clearInterval(timer); // setInterval 중지

    // 새로운 기록 요소 생성
    const record = document.createElement('div');
    const checkButton = document.createElement('button');
    const recordContent = document.createElement('h3');
    const blankbox = document.createElement('div');

    recordContent.innerHTML = time.innerHTML;
    record.classList.add('record');
    checkButton.classList.add('check_button');
    blankbox.classList.add('blankbox');
    recordContent.classList.add('record_content');

    // 체크 버튼 클릭 로직
    checkButton.addEventListener('click', () => {
        checkButton.classList.toggle('checked'); // 체크 상태 토글
        checkButton.innerHTML = checkButton.classList.contains('checked') ? '✔️' : ''; // 체크 표시
    });

    // 구성 요소 추가
    record.appendChild(checkButton);
    record.appendChild(recordContent);
    record.appendChild(blankbox);
    recordList.appendChild(record);

    // 스크롤 자동 이동
    recordContainer.scrollTop = recordContainer.scrollHeight;
}

// 3. 스톱워치 초기화
function reset() {
    s = 0;
    ms = 0;
    time.innerHTML = '00:00';
    clearInterval(timer);
}

// 4. 스톱워치 시간 업데이트
function Timer() {
    ms += 1; // 10ms 증가

    if (ms >= 100) {
        ms = 0; // 밀리초 리셋
        s += 1; // 초 증가
    }

    if (s >= 60) {
        s = 0; // 초 리셋
    }

    // 화면에 표시
    const formattedS = s < 10 ? '0' + s : s; // 2자리 포맷
    const formattedMs = ms < 10 ? '0' + ms : ms; // 2자리 포맷

    time.innerHTML = formattedS + ':' + formattedMs;
}

// 5. 상단 전체 선택 버튼 로직
checkAllButton.addEventListener('click', () => {
    const checkButtons = document.querySelectorAll('.check_button');
    const isAllChecked = Array.from(checkButtons).every(button => button.classList.contains('checked'));

    // 전체 체크/해제
    checkButtons.forEach(button => {
        if (isAllChecked) {
            button.classList.remove('checked'); // 해제
            button.innerHTML = ''; // 체크 표시 제거
        } else {
            button.classList.add('checked'); // 체크
            button.innerHTML = '✔️'; // 체크 표시 추가
        }
    });

    // 상단 버튼 상태도 동기화
    checkAllButton.classList.toggle('checked', !isAllChecked);
    checkAllButton.innerHTML = checkAllButton.classList.contains('checked') ? '✔️' : ''; // 상단 버튼 표시
});

// 6. 상단 휴지통 버튼 로직
deleteButton.addEventListener('click', () => {
    const checkedRecords = document.querySelectorAll('.record .check_button.checked');
    const checkedAllButton = document.querySelector('.check_button_all');
    // 체크된 기록 삭제
    checkedRecords.forEach(button => {
        button.parentElement.remove();
    });
    checkedAllButton.classList.remove('checked');
    checkAllButton.innerHTML = checkAllButton.classList.contains('checked') ? '✔️' : ''; // 상단 버튼 표시
});