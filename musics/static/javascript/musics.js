
document.querySelectorAll('.musics').forEach(el => {

    el.addEventListener('click', () => {
        window.location.href = `http://127.0.0.1:8000/update/${el.dataset.id}`;
    });

});

document.querySelectorAll('.publicado').forEach(el => {

    if (el.innerHTML == 0) {
        el.innerHTML = 'Não';
    } else {
        el.innerHTML = 'Sim';
    }

});

document.querySelectorAll('.minutes').forEach(el => {

    let seconds = el.innerHTML;
    let minutes = parseInt(seconds / 60);
    let timeLeft = seconds % 60;
    console.log(formatTime(minutes) + ':' + formatTime(timeLeft))
    el.innerHTML = formatTime(minutes) + ':' + formatTime(timeLeft);
    
});

function formatTime(el) {

    if (el.toString().length == 1) {
        el = '0' + el.toString();
    }
    return el;
}