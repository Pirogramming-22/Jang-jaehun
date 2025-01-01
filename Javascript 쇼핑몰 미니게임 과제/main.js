// JSON file로부터 데이터를 받아와서, 데이터를 화면에 렌더링하는 기능을 구현
function loadItems() {
    return fetch('data/data.json')
        .then(response => response.json())
        .then(json => json.items);
}

// main
loadItems()
    .then(items => {
        console.log(items);
        // displayItems(items);
        // setEventListeners(items);
    })
    .catch(console.log);