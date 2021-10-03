var numeroSecreto = parseInt(Math.random() * 11);
var resultadoFinal = document.getElementById("resultado");
var chances = 3;
var chute2 = document.getElementById("chute");

function Chutar() {
  var chute = parseInt(document.getElementById("valor").value);

  if (chances > 0) {
    if (chute == numeroSecreto) {
      var chute2 = document.getElementById("chute");
      chute2.disabled = true;
      resultadoFinal.innerHTML =
        "Parabéns! Você acertou o número secreto! Clique em Recomeçar para jogar novamente!";
    } else if (chute < 0 || chute > 10) {
      resultadoFinal.innerHTML = "Por favor, digite um número entre 0 e 10!";
    } else if (chute < numeroSecreto) {
      chances = chances - 1;
      resultadoFinal.innerHTML =
        "O número é maior que este valor! Tente novamente";
    } else if (chute > numeroSecreto) {
      chances = chances - 1;
      resultadoFinal.innerHTML =
        "O número é menor que este valor! Tente novamente";
    }
  }
  if (chances == 0) {
    var chute2 = document.getElementById("chute");
    chute2.disabled = true;
    resultadoFinal.innerHTML =
      "Você perdeu! O número secreto era " + numeroSecreto;
  }
}

function Recomeçar() {
  chute2.disabled = false;
  var resultadoFinal = document.getElementById("resultado");
  numeroSecreto = parseInt(Math.random() * 11);
  resultadoFinal.innerHTML = "Vamos lá!";
  chances = 3;
}
