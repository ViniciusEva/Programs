const ElementosExercicio = document.querySelectorAll(".exercicio");
const ElementoTela = document.querySelector(".tela");
const ElementoVoltar = document.querySelector(".voltar");
const ElementoClose = document.querySelector(".close");
const ElementoPlay = document.querySelector(".play");
const ElementoPause = document.querySelector(".pause");
const ElementoCronometro = document.querySelector(".cronometro");
const ElementoHorario = document.querySelector(".horario");
const ElementoMinuto = document.querySelector(".minuto");
const ElementoSegundo = document.querySelector(".segundo");
const ElementoCentesimo = document.querySelector(".centesimo")

var timer = 0;
var idintervalo = null;


//Adiconar classa, tela e cronometro
ElementosExercicio.forEach(function(ElementoExercicio) {
  ElementoExercicio.addEventListener("click", function () {
    ElementoTela.classList.add("tela--cronometro"); //mudar de tela
    //console.log("clicou!");
  });
});

ElementoVoltar.addEventListener("click", function () {
  ElementoTela.classList.remove("tela--cronometro"); //mudar de tela

  clicouClose();
});

//console.log(ElementoExercicio);

//adicionar classe iniciou
function clicouClose() {
  ElementoCronometro.classList.remove("iniciou");
  
  timer = 0;
  clearInterval(idintervalo);
  atualizarCronometro();
}

ElementoClose.addEventListener("click", function () {
    clicouClose();
});

ElementoPlay.addEventListener("click", function () {
    ElementoCronometro.classList.add("iniciou");
});

function clicouPlay() {
  ElementoCronometro.classList.add("iniciou");

  rodarTimer();
}

ElementoPlay.addEventListener("click", function(){
  clicouPlay();
});

function clicouPause() {
  ElementoCronometro.classList.remove("iniciou");

  clearInterval(idintervalo);
}

ElementoPause.addEventListener("click", function () {
    clicouPause();
});

//Atualizar Horário
function atualizarHorario() {
    const horas = new Date().getHours().toString().padStart(2, "0");
    const minutos = new Date().getMinutes().toString().padStart(2, "0");
    const horario = horas + ":" + minutos;

    ElementoHorario.innerText = horario;
    //console.log(horario);
}

atualizarHorario();

setInterval(() => {
  atualizarHorario();
}, 1000);  /*1000 minlésimo (1 segundo) timer*/


//Construindo o Cronômetro
function rodarTimer() {
  idintervalo = setInterval(() => {
    timer = timer + 10;
    //console.log("timer");
    atualizarCronometro();
  }, 10);
}

function atualizarCronometro() {
  const minutos = Math.floor(timer/60000).toString().padStart(2, "0");
  const segundos = Math.floor((timer % 60000) / 1000).toString().padStart(2, "0");
  const centesimos = Math.floor(((timer % 60000) % 1000) / 10).toString().padStart(2,"0");
  const tempoCronometro = minutos + ":" + segundos + "," + centesimos;

  ElementoMinuto.innerText = minutos;
  ElementoSegundo.innerText = segundos;
  ElementoCentesimo.innerText = centesimos;

  console.log(tempoCronometro);
}