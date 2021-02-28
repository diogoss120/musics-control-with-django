class Form {
    constructor() {
        this.btnDelete = document.querySelector('.btnDelete');
        this.btnSubmit = document.querySelector('.btnSubmit');
        this.form = document.querySelector('form');
        this.validacaoForm();
        this.eventosCheckbox();
        this.ajustes();
    }

    validacaoForm() {
        let msgSuccess = 'Música adicionada com sucesso!';

        if (this.btnDelete) {

            msgSuccess = 'Música alterada com sucesso!';
            this.btnDelete.addEventListener('click', event => {
                let id = this.form.dataset.idmusic;
                window.location.href = `http://127.0.0.1:8000/delete/${id}`;
                alert('Música apagada com sucesso!');
            });

        }

        this.btnSubmit.addEventListener('click', event => {

            if (this.formValido(event)) {
                alert(msgSuccess);
            }

        });

    }

    ajustes(){
        document.querySelector('label[for="id_duration"]').innerHTML = `Duration/Seconds`;
    }

    formValido(event) {
        let formValido = true;

        this.form.querySelectorAll('input[type="text"]').forEach(el => {

            if (el.value == '') {
                formValido = false;
            }

        });

        this.form.querySelectorAll('input[type="number"]').forEach(el => {
            if (parseInt(el.value) < 60) {
                event.preventDefault()
                formValido = false;
                alert('Música com tempo de duração muito curto\nTem que ter acima de 1 minuto')
            } else if (el.value == '') {
                formValido = false;
            }
        });

        this.form.querySelectorAll('select').forEach(el => {

            if (el.value == '') {
                formValido = false;
            }

        });

        return formValido;
    }

    eventosCheckbox() {
        document.querySelectorAll('input[type="checkbox"]').forEach(el => {
            //pega o paragrafo pai do input type checkbox
            this.paragrafo = el.parentElement;

            this.paragrafo.className = 'checkbox';

            this.paragrafo.addEventListener('click', e => {
                el.click();
            });

            el.addEventListener('click', e => {
                el.click();
            });

            //pega o primeiro elemento que está dentro do pararafo, nesse caso a label
            this.paragrafo.firstElementChild.addEventListener('click', e => {
                el.click();
            });

        });
    }
}

let form = new Form();