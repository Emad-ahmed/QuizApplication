
const modalBtns = [...document.getElementsByClassName('modal-button')]


const modalBody = document.getElementById("modal-body-confirm");

const startBtn = document.getElementById("start-button");

const url = window.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=> {
    const pk = modalBtn.getAttribute('data-pk');
    const name = modalBtn.getAttribute('data-quiz');
    const numQuestion = modalBtn.getAttribute('data-questions');
    const difficulty = modalBtn.getAttribute('data-difficulty');
    const scoreToPass = modalBtn.getAttribute('data-pass');
    const time = modalBtn.getAttribute('data-time');

    modalBody.innerHTML = `
    <div class="h5 mb-5">
    Are You Sure You Want To Begin
    "<b>${name}</b>"

    <div class="text-muted mt-4">
        <ul>
        <li>Difficulty: <b>${difficulty}</b></li>
        <li>Number Of Questions: <b>${numQuestion}</b></li>
        <li>Score To Pass: <b>${scoreToPass}</b></li>
        <li>Time: <b>${time} min</b></li>
        </ul>
    </div>
    </div>
    `

    startBtn.addEventListener('click', ()=>{
    
       window.location.href = url + pk;
    });
    
}));


