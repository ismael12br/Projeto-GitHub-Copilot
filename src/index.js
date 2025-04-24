function validarCartao(numeroCartao) {
    const bandeiras = [
        { nome: "Visa", regex: /^4\d{12}(\d{3})?$/ },
        { nome: "MasterCard", regex: /^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$/ },
        { nome: "Elo", regex: /^(4011|4312|4389|5041|5066|509|6277|6362|6363|650|651|652|655)\d*$/ },
        { nome: "American Express", regex: /^3[47]\d{13}$/ },
        { nome: "Discover", regex: /^(6011\d{12}|65\d{14}|64[4-9]\d{13})$/ },
        { nome: "Hipercard", regex: /^6062\d{12}$/ }
    ];

    for (const bandeira of bandeiras) {
        if (bandeira.regex.test(numeroCartao)) {
            return bandeira.nome;
        }
    }

    return "Bandeira desconhecida";
}

// Exemplo de uso:
const numeroCartao = "3504166307884548"; // Substitua pelo número do cartão a ser testado
const bandeira = validarCartao(numeroCartao);
console.log(`Bandeira do cartão: ${bandeira}`);