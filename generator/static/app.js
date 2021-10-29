document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form');
    const length = document.getElementById('length');
    const p = document.createElement('p');

    form.onsubmit = function (e) {
        e.preventDefault();



        if (Number(length.value) < 8) {
            p.classList.add('alert', 'alert-danger')
            p.innerText = 'Choose at least 8 chars';
            length.classList.add('is-invalid')
            if (!length.parentElement.contains(p)) {
                length.parentElement.appendChild(p)
            }
            length.focus();
            length.onblur = () => length.focus();
            return;
        }

        form.submit();
    }

    length.onkeyup = function(e){
        const {value} = e.target;
        if(Number(value) >= 8 && length.parentElement.contains(p)){
            length.parentElement.removeChild(p)
        }else if (Number(value) < 8){
            length.parentElement.appendChild(p)
        }
    }

})