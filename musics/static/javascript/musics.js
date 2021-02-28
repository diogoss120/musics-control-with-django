class Music {
    constructor() {
        this.events();
    }

    events() {
        let musicas = document.querySelectorAll('.musics');

        console.log(musicas.length);
        if (musicas.length > 0) {

            musicas.forEach(el => {

                el.addEventListener('click', () => {
                    window.location.href = `http://127.0.0.1:8000/update/${el.dataset.id}`;
                });

            });
        } else {
            document.querySelector('.container').innerHTML =
                `<span>Este artista não possui músicas registradas</span>`;
        }

        document.querySelectorAll('.publicado').forEach(el => {

            if (el.innerHTML == 0) {
                el.innerHTML = 'Não';
            } else {
                el.innerHTML = 'Sim';
            }

        });

        document.querySelectorAll('.minutes').forEach(el => {

            let seconds = parseInt(el.innerHTML);
            el.innerHTML = this.formatTime(seconds);

        });
    }

    formatTime(time) {

        var hours = Math.floor(time / 3600);
        var minutes = Math.floor((time % 3600) / 60);
        var seconds = time % 60;

        minutes = minutes < 10 ? '0' + minutes : minutes;
        seconds = seconds < 10 ? '0' + seconds : seconds;
        hours = hours < 10 ? '0' + hours : hours;

        if (parseInt(hours) > 0) {
            return hours + ":" + minutes + ":" + seconds;
        }

        return minutes + ":" + seconds;

    }
}

let music = new Music();