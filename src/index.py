import re

def luhn_check(card_number):
    """
    Verifica se o número do cartão é válido usando o algoritmo de Luhn.
    
    Args:
        card_number (str): Número do cartão de crédito.
    
    Returns:
        bool: True se o número for válido, False caso contrário.
    """
    digits = [int(d) for d in card_number]
    checksum = 0
    parity = len(digits) % 2
    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

def is_valid_format(card_number):
    """
    Verifica se o número do cartão está no formato válido (13 a 19 dígitos).
    
    Args:
        card_number (str): Número do cartão de crédito.
    
    Returns:
        bool: True se o formato for válido, False caso contrário.
    """
    return re.fullmatch(r'\d{13,19}', card_number) is not None

def get_card_brand(card_number):
    """
    Identifica a bandeira do cartão de crédito com base no número.
    
    Args:
        card_number (str): Número do cartão de crédito.
    
    Returns:
        str: Nome da bandeira ou 'Desconhecida' se não for encontrada.
    """
    brands = {
        'Visa': r'^4\d{12}(\d{3})?$',
        'Mastercard': r'^(5[1-5]\d{14}|2(2[2-9]\d{12}|[3-6]\d{13}|7[01]\d{12}|720\d{12}))$',
        'American Express': r'^3[47]\d{13}$',
        'Discover': r'^(6011\d{12}|65\d{14}|64[4-9]\d{13}|622(12[6-9]|1[3-9]\d|[2-8]\d{2}|9[01]\d|92[0-5])\d{10})$',
        'JCB': r'^35(2[8-9]|[3-8][0-9])\d{12,15}$',
        'Elo': r'^(4011|4312|4389|5041|5066|509|6277|6362|6363|650|651|652|655|636368|438935|504175|451416|636297|5067|4576|506699)\d*$',
        'Hipercard': r'^(606282|3841)\d*$',
        'Diners Club': r'^3(0[0-5]|[68]\d)\d{11}$',
        'Aura': r'^50\d{14}$',
        'Visa Electron': r'^(4026|417500|4508|4844|4913|4917)\d*$',
        'UATP': r'^1\d{14}$',
        'Verve': r'^(506099|5061\d{2}|650002|650027|507865|507964)\d*$',
        'LankaPay': r'^357111\d*$',
        'RuPay': r'^(353|356)\d*$',
        'InterPayment': r'^636\d*$',
        'InstaPayment': r'^637|639\d*$',
        'Voyager': r'^8699\d{11}$',  # Adicionada bandeira Voyager
        'EnRoute': r'^(2014|2149)\d{11}$'  # Adicionada bandeira EnRoute
    }
    for brand, pattern in brands.items():
        if re.match(pattern, card_number):
            return brand
    return 'Desconhecida'

def format_card_number(card_number):
    """
    Remove os espaços de um número de cartão de crédito.
    
    Args:
        card_number (str): Número do cartão de crédito com espaços.
    
    Returns:
        str: Número do cartão de crédito sem espaços.
    """
    return card_number.replace(" ", "")

def main():
    """
    Solicita o número do cartão de crédito ao usuário, valida o formato, 
    verifica o algoritmo de Luhn e identifica a bandeira.
    """
    card_number = input("Digite o número do cartão: ").strip()
    card_number = format_card_number(card_number)  # Remove os espaços
    if is_valid_format(card_number) and luhn_check(card_number):
        brand = get_card_brand(card_number)
        print(f"Bandeira: {brand}")
    else:
        print("Número de cartão inválido.")

if __name__ == "__main__":
    main()
