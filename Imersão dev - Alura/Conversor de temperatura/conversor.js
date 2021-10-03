// var nome = "Ramon"
// var notaDoPrimeiroBimestre = 7
// var notaDoSegundoBimestre = 7
// var notaDoTerceiroBimestre = 8
// var notaDoQuartoBimestre = 9
// var notaFinal = (notaDoPrimeiroBimestre + notaDoSegundoBimestre + notaDoTerceiroBimestre + notaDoQuartoBimestre) / 4

// var notaCorrigida = notaFinal.toFixed(2)

// console.log("Bem vindo " + nome)
// console.log(notaCorrigida)

//Está é uma revisão

//Variável: São espaços alocados na mémoria para armazenar algum valor.
// String: Uma variável de texto, todo conteudo dentro de "" são considerados strings e tradados como texto.
// Console.log: Função utilizada para imprimir/escrever/retornar variavel para o console
//to.Fixed: Comando utilizado para fixar a quantidade de casas decimais que será exibida no console
// Operadores matematicos: + Soma; - Subtração; * Multiplicação; / Divisão; seguem a precedência operadores, por isso é importante se atentar a ordem logica em que a operação será processada
// Concatenação: Junção/relacionamento/encadeamento/agrupamento

// Desafio - Exibir resulatdo de aprovado ou reprovado

var notaB1 = 8
var notaB2 = 5
var notaB3 = 8
var notaB4 = 5
 
var notaFinal = (notaB1+notaB2+notaB3+notaB4)/4

var notaCorrigida = notaFinal.toFixed(0)


if (notaCorrigida >= 6)
  console.log("Sua nota foi "+ notaCorrigida + " você foi aprovado")
else
  console.log("Sua nota foi " + notaCorrigida + "você foi reprovado")

// Desafio - Converter de celsius para fahrenheit

var temperatura = 32

var fahrenheit = (temperatura * 9/5) + 32

console.log(temperatura + " Em graus celsius equivale a "+fahrenheit +" graus fahrenheit")

