function update_list() {
    console.log('ready');
    fetch(
        /* Путь к серверу. Он может быть
        с доменом: http(s):////
        абсолютный (на этом домене)
        относительный (на этом домене) */
        '/tasklist/update_tasks/', {
        method: "post" ,
        body: JSON.stringify({
            param_pam_pam: "Val"
        }),
        headers: {
            'X-CSRFToken': document.querySelector(
                '[name=csrfmiddlewaretoken]').value
        }
    }
    ).then((data) => {
        if (true) {  //data.status == 200)
            console.log('RESPONSE!');
            return data.json();  // Мы просто знаем...
            // А надо БРАТЬ тип данных!!!
        }
    }).then((datajson) => {
        console.log(datajson);
        console.log(datajson['mydata']);
        for (let newtask of datajson['tasks']) {
            console.log('Добавляю:', newtask);
            add_elem_to_list(newtask);
        }
    });
    //add_elem_to_list('Молодец, но это легко!');
}

function add_elem_to_list(txt) {
    //  1 можно                 2 НЕЛЬЗЯ!
    let li = document.createElement('li');
    let txtn = document.createTextNode(txt);
    li.appendChild(txtn);
    // let all_tasks = document.getElementById(
    //    'all_tasks');
    all_tasks.appendChild(li);
}

window.addEventListener(
    /* После загрузки страницы запустить функцию update_list */
    'load',
    () => {
//        update_list();
//        window.setInterval(
        window.setTimeout(
            update_list,  // Функция, которая будет работать по таймеру
            15000          // 5 тысяч миллисекунд
        );
    } 
    /* это НЕ ВЫЗОВ, а передача функции для позднего вызова при наступлении события */
);