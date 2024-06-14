// Função para calcular o fatorial de um número
function calcularFatorial(num) {
    if (num < 0) {
        return "Número deve ser inteiro positivo.";
    }
    let fatorial = 1;
    for (let i = 1; i <= num; i++) {
        fatorial *= i;
    }
    return fatorial;
}

// Função para calcular a sequência de Fibonacci até um determinado número
function calcularFibonacci(num) {
    if (num < 0) {
        return "Número deve ser inteiro positivo.";
    }
    let fibonacci = [0, 1];
    for (let i = 2; i <= num; i++) {
        fibonacci.push(fibonacci[i - 1] + fibonacci[i - 2]);
    }
    return fibonacci.slice(0, num + 1); // Ajustar o tamanho da sequência até o número fornecido
}

// Função principal
function main() {
    let numero = parseInt(prompt("Digite um número inteiro positivo:"));

    if (isNaN(numero) || numero < 0) {
        console.log("Por favor, digite um número inteiro positivo.");
        return;
    }

    // Calcular e exibir o fatorial
    let fatorial = calcularFatorial(numero);
    console.log(`Fatorial de ${numero}: ${fatorial}`);

    // Calcular e exibir a sequência de Fibonacci
    let fibonacci = calcularFibonacci(numero);
    console.log(`Sequência de Fibonacci até ${numero}: ${fibonacci.join(", ")}`);
}

// Executar o programa principal
main();
