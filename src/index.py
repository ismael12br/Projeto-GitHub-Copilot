import re

def formatar_numero_cartao(numero_cartao):
    """
    Remove os espaços de um número de cartão de crédito.
    
    Args:
        numero_cartao (str): Número do cartão de crédito com espaços.
    
    Returns:
        str: Número do cartão de crédito sem espaços.
    """
    return numero_cartao.replace(" ", "")

def validar_cartao(numero_cartao):
    """
    Valida o número do cartão de crédito e identifica a bandeira.
    
    Args:
        numero_cartao (str): Número do cartão de crédito sem espaços.
    
    Returns:
        str: Nome da bandeira do cartão ou None se não for encontrada.
    """
    bandeiras = [
        {"nome": "Visa", "regex": r"^4\d{12}(\d{3})?$"},
        {"nome": "MasterCard", "regex": r"^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$"},
        {"nome": "Elo", "regex": r"^(4011|4312|4389|5041|5066|509|6277|6362|6363|650|651|652|655|636368|438935|504175|451416|636297|5067|4576|506699)\d*$"},
        {"nome": "American Express", "regex": r"^3[47]\d{13}$"},
        {"nome": "Discover", "regex": r"^(6011\d{12}|65\d{14}|64[4-9]\d{13}|622(12[6-9]|1[3-9]\d|[2-8]\d{2}|9[01]\d|92[0-5])\d{10})$"},
        {"nome": "Hipercard", "regex": r"^(606282|3841)\d*$"},
        {"nome": "Diners Club", "regex": r"^3(0[0-5]|[68]\d)\d{11}$"},
        {"nome": "JCB", "regex": r"^35(2[8-9]|[3-8][0-9])\d{12,15}$"},
        {"nome": "Aura", "regex": r"^50\d{14}$"},
        {"nome": "Visa Electron", "regex": r"^(4026|417500|4508|4844|4913|4917)\d*$"},
        {"nome": "UATP", "regex": r"^1\d{14}$"},
        {"nome": "Verve", "regex": r"^(506099|5061\d{2}|650002|650027|507865|507964)\d*$"},
        {"nome": "LankaPay", "regex": r"^357111\d*$"},
        {"nome": "UzCard", "regex": r"^8600\d*$"},
        {"nome": "Humo", "regex": r"^9860\d*$"},
        {"nome": "RuPay", "regex": r"^(353|356)\d*$"},
        {"nome": "InterPayment", "regex": r"^636\d*$"},
        {"nome": "InstaPayment", "regex": r"^637|639\d*$"}
    ]

    for bandeira in bandeiras:
        if re.match(bandeira["regex"], numero_cartao):
            return bandeira["nome"]

    return None

def solicitar_numero_cartao():
    """
    Solicita o número do cartão de crédito ao usuário, remove espaços e valida a bandeira.
    """
    while True:
        try:
            numero_cartao = input("Digite o número do cartão de crédito: ").strip()
            numero_cartao = formatar_numero_cartao(numero_cartao)  # Remove os espaços
            if not numero_cartao.isdigit():
                raise ValueError("O número do cartão deve conter apenas dígitos.")
            
            bandeira = validar_cartao(numero_cartao)
            if bandeira:
                print(f"Bandeira do cartão: {bandeira}")
                break
            else:
                print("Bandeira não encontrada. Digite novamente.")
        except ValueError as e:
            print(e)

# Execução principal
if __name__ == "__main__":
    solicitar_numero_cartao()