var CHANGE_TIME = 5;
function change_opacity(element, opacity, num) {
                "use strict";
    setTimeout(function() {
        element.style.opacity = opacity;
    }, CHANGE_TIME / 2 * num * 10);
}

function replace_text(element, text) {
    "use strict";
    var cur_opacity = 1.0;
    var num = 1;
    for (; cur_opacity >= 0; cur_opacity -= 0.01) {
        change_opacity(element, cur_opacity, num);
        num += 1;
    }
    var item = text[Math.floor(Math.random()*text.length)];
    setTimeout(function() {
        element.textContent = item;
    }, CHANGE_TIME / 2 * num * 10);
    for (; cur_opacity <= 1; cur_opacity += 0.01) {
        change_opacity(element, cur_opacity, num);
        num += 1;
    }
}

function loading(){
    "use strict";
    document.getElementById('main_part').style.display='none';
    var load = document.getElementById('loading');
    load.style.display = 'block';
    load.textContent = 'Ждемс...';
    //TODO: load from /loading_texts
    var messages = [
            "Ищем мудрецов...",
            "Спрашиваем мудрецов...",
            "Анализируем мудрецов...",
            "Перезагружаем интернет...",
            "Перекладываем jsonы...",
            "Балабобим...",
            "Работаем...",
            "Правда работаем...",
            "Еще работаем...",
            "Решаем проблемы...",
            "Вызываем /viber..."];
    setInterval(replace_text, CHANGE_TIME * 1000, load, messages);
}