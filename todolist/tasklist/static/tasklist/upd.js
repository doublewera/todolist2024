function update_list() {
    console.log('ready');
    fetch('/tasklist/update_tasks/'
    ).then((data) => {
        if (true) {  //data.status == 200)
            console.log('RESPONSE!');
            return data.json();
        }
    }).then((datajson) => {
        console.log(datajson);
        console.log(datajson['mydata']);
        add_elem_to_list(datajson['mydata']);
    });
    add_elem_to_list('Молодец, но это легко!');
}

function add_elem_to_list(txt) {
    let li = document.createElement('li');
    let txtn = document.createTextNode(txt);
    li.appendChild(txtn);
    all_tasks.appendChild(li);
}

window.addEventListener(
    'load',
    update_list
);