document.querySelectorAll('.tr-artist').forEach(function (el) {
    el.addEventListener('click', e => {
        window.location.href = `http://127.0.0.1:8000/musics/${el.dataset.id}`;
    })
});
