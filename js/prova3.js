// Função para solicitar e obter a entrada do usuário
function obterEntrada(mensagem) {
    return prompt(mensagem);
}

// Função principal
function main() {
    // Solicitar o número total de estudantes
    let totalEstudantes = parseInt(obterEntrada("Digite o número total de estudantes na turma:"));

    // Inicializar variáveis para armazenar a soma das notas, a maior nota e a menor nota
    let somaNotas = 0;
    let maiorNota = -Infinity;
    let menorNota = Infinity;

    // Loop para solicitar e processar as notas de cada aluno
    for (let i = 1; i <= totalEstudantes; i++) {
        let nota = parseFloat(obterEntrada(`Digite a nota do aluno ${i}:`));

        // Atualizar a soma das notas
        somaNotas += nota;

        // Verificar se a nota atual é a maior ou a menor
        if (nota > maiorNota) {
            maiorNota = nota;
        }
        if (nota < menorNota) {
            menorNota = nota;
        }
    }

    // Calcular a média da turma
    let media = somaNotas / totalEstudantes;

    // Exibir os resultados
    console.log("Média da turma:", media.toFixed(2));
    console.log("Maior nota:", maiorNota);
    console.log("Menor nota:", menorNota);
}

// Executar o programa principal
main();
