// script.js
const calcularGorjeta = () => {
    const totalConta = parseFloat(document.getElementById('total-conta').value);
    const qualidadeServico = parseFloat(document.getElementById('qualidade-servico').value);

    if (isNaN(totalConta) || totalConta <= 0) {
        alert('Por favor, digite um valor válido para o total da conta.');
        return;
    }

    const gorjeta = calcularPorcentagem(totalConta, qualidadeServico);
    const totalPagar = totalConta + gorjeta;

    exibirResultado(gorjeta, totalPagar);
};

const calcularPorcentagem = (valor, percentual) => {
    return valor * percentual;
};

const exibirResultado = (gorjeta, totalPagar) => {
    const resultadoElement = document.getElementById('resultado');
    resultadoElement.innerHTML = `
      <h3>Valor da Gorjeta: R$ ${gorjeta.toFixed(2)}</h3>
      <h3>Total a Pagar: R$ ${totalPagar.toFixed(2)}</h3>
    `;
};
