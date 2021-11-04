let ordem = [];
let ordemDeClique = [];
let pontos = 0;

// 0 - amarelo
// 1 - azul
// 2 - verde
// 3 - vermelho

const amarelo = document.querySelector('.amarelo');
const azul = document.querySelector('.azul');
const verde = document.querySelector('.verde');
const vermelho = document.querySelector('.vermelho');

//cria ordem aletoria de cores
let ordemEmbaralhada = () => {
    let ordemDeCores = Math.floor(Math.random() * 4);
    ordem[ordem.length] = ordemDeCores;
    ordemDeClique = [];

    for (let i in ordem) {
        let elementoCor = crieElementoCor(ordem[i]);
        brilho(elementoCor, Number(i) + 1);
    }
}

//acende a proxima cor
let brilho = (element, number) => {
    number = number * 300;
    setTimeout(() => {
        element.classList.add('selected');
    }, number - 250);
    setTimeout(() => {
        element.classList.remove('selected');
    });
}

//checa se os botoes clicados são os mesmos da ordem gerada no jogo
let verificarOrdem = () => {
    for (let i in ordemDeClique) {
        if(ordemDeClique [i] != ordem[i]){
            fimDeJogo();
            break;
        }
    }
    if(ordemDeClique.length == ordem.length){
        alert(`Pontuação: ${pontos}\n Você acertou!! Iniciando próxima nível!`);
        proximoNivel();
    }
}

//funcao para o clique do usuario
let clique = (cor) => {
    ordemDeClique[ordemDeClique.length] = cor;
    crieElementoCor(cor).classList.add('selected');

    setTimeout(() => {
        crieElementoCor(cor).classList.remove('selected');
        verificarOrdem();
    }, 250);
}

//funcao que retorna a cor
let crieElementoCor = (cor) =>{
    if(cor == 0) {
        return amarelo;
    } else if(cor == 1) {
        return azul;
    } else if (cor == 2) {
        return verde;
    } else if (cor == 3) {
        return vermelho;
    }
}

//funcao para proximo nivel do jogo
let proximoNivel = () => {
    pontos++;
    ordemEmbaralhada();
}

//funcao para fim de jogo
let fimDeJogo = () => {
    alert(`Pontuação: ${pontos}!\nVocê perdeu o jogo!\nClique em OK para iniciar um novo jogo`);
    ordem = [];
    ordemDeClique = [];

    Jogar();
}

//funcao de inicio do jogo
let Jogar = () => {
    alert('Bem vindo ao Genius! Iniciando novo jogo!');
    pontos = 0;

    proximoNivel();
}

//eventos de clique para as cores

amarelo.onclick = () => clique(0);
azul.onclick = () => clique(1);
verde.onclick = () => clique(2);
vermelho.onclick = () => clique(3);


//inicio do jogo
Jogar();

