
document.querySelectorAll('.musics').forEach( el => {
    el.addEventListener('click', () => {
        window.location.href = `http://127.0.0.1:8000/update/${el.dataset.id}`;
    });
})