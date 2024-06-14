// script.js
function calcularIMC() {
    // Obter os valores de peso e altura dos inputs
    let peso = document.getElementById('peso').value;
    let altura = document.getElementById('altura').value;

    // Converter os valores para números
    peso = parseFloat(peso);
    altura = parseFloat(altura);

    // Verificar se os valores são válidos (números positivos)
    if (isNaN(peso) || isNaN(altura) || peso <= 0 || altura <= 0) {
        alert('Por favor, digite valores válidos para peso e altura.');
        return;
    }

    // Calcular o IMC
    let imc = peso / (altura * altura);

    // Exibir o resultado na tela
    let resultado = document.getElementById('resultado');
    resultado.innerHTML = `<h3>Seu IMC é: ${imc.toFixed(2)}</h3>`;

    // Exibir a classificação do IMC
    if (imc < 18.5) {
        resultado.innerHTML += `<p>Classificação: Abaixo do peso</p>`;
    } else if (imc < 25) {
        resultado.innerHTML += `<p>Classificação: Peso normal</p>`;
    } else if (imc < 30) {
        resultado.innerHTML += `<p>Classificação: Sobrepeso</p>`;
    } else {
        resultado.innerHTML += `<p>Classificação: Obesidade</p>`;
    }
}
