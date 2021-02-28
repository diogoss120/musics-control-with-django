class Base{
    constructor(){
        this.events();
    }

    events(){
        document.querySelectorAll('li.artist').forEach(el => {
            el.addEventListener('click', e => {
                window.location.href = `http://127.0.0.1:8000/musics/${el.dataset.id}`;
            })
        });

        document.getElementById('url_new_song').addEventListener('click', () => {
            window.location.href = `http://127.0.0.1:8000/new`;
        });

        document.getElementById('url_home').addEventListener('click', () => {
            window.location.href = `http://127.0.0.1:8000`;
        });
    }
}

let base = new Base();