// Função para solicitar e obter a entrada do usuário
function obterEntrada(mensagem) {
    return prompt(mensagem);
}

// Função para calcular o IMC
function calcularIMC(peso, alturaCm) {
    let alturaM = alturaCm / 100; // Convertendo centímetros para metros
    return peso / (alturaM * alturaM);
}

// Função para classificar o IMC
function classificarIMC(imc) {
    if (imc < 16) {
        return "Baixo peso muito grave";
    } else if (imc >= 16 && imc <= 16.99) {
        return "Baixo peso grave";
    } else if (imc >= 17 && imc <= 18.49) {
        return "Baixo peso";
    } else if (imc >= 18.50 && imc <= 24.99) {
        return "Peso normal";
    } else if (imc >= 25 && imc <= 29.99) {
        return "Sobrepeso";
    } else if (imc >= 30 && imc <= 34.99) {
        return "Obesidade grau I";
    } else if (imc >= 35 && imc <= 39.99) {
        return "Obesidade grau II";
    } else {
        return "Obesidade grau III";
    }
}

// Função principal
function main() {
    let nome = obterEntrada("Digite seu nome:");
    let alturaCm = parseFloat(obterEntrada("Digite sua altura em centímetros:"));
    let peso = parseFloat(obterEntrada("Digite seu peso em kg:"));

    let imc = calcularIMC(peso, alturaCm);
    let classificacao = classificarIMC(imc);

    console.log("Nome:", nome);
    console.log("IMC:", imc.toFixed(2));
    console.log("Classificação:", classificacao);
}

// Executar o programa principal
main();
