class Form {
    constructor() {
        this.btnDelete = document.querySelector('.btnDelete');
        this.btnSubmit = document.querySelector('.btnSubmit');
        this.form = document.querySelector('form');
        this.validacaoForm();
        this.eventosCheckbox();
    }

    validacaoForm() {

        if (this.btnDelete) {

            this.btnDelete.addEventListener('click', e => {
                let id = this.form.dataset.idmusic;
                window.location.href = `http://127.0.0.1:8000/delete/${id}`;
                alert('Música apagada com sucesso!');
            });

            this.btnSubmit.addEventListener('click', e => {

                if (this.formValido()) {
                    alert('Música alterada com sucesso!');
                } else {
                    e.preventDefault()
                }
            });

        } else {
            this.btnSubmit.addEventListener('click', e => {
                alert('Música adicionada com sucesso!');
            });
        }
    }

    formValido() {
        let formValido = true;
        this.form.querySelectorAll('input[type="text"], input[type="number"], select').forEach(el => {

            if (el.value == '') {
                formValido = false;
            }

            if (el.type == 'number' && parseInt(el.value) < 60) {
                formValido = false;
                alert('Não existe uma música com esse tempo de duração')
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