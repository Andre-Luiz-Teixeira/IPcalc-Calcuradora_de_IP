import Decimal


def DecBin(Transformar):
    Lista = Transformar.split('.')

    Transformado = ''  # string de ip binario
    j = 3  # 4 octeto
    while j >= 0:
        # Seleciona o octeto
        temp = int(Lista[j])  # transforma um pedaço do octeto em inteiro decimal
        i = 7  # 8 bits
        while i >= 0:
            # Gerador do binario por octeto
            Bit = int(temp % 2)  # coleta o inteiro do mod
            Transformado = str(Bit) + Transformado  # concatena o resultado na string
            temp = temp / 2  # captura o proximo numero a ser transformado em 0 ou 1
            i = i - 1
        if j != 0:
            Transformado = '.' + Transformado  # string armazenadora
        j = j - 1

    return Transformado


def BinIP(IP):
   return DecBin(IP)


def BinMask(CIDR):
    # calcula a mascara para uma string binaria
    m = 0
    contador = 0
    maskbin = ''  # string de mascara binaria

    while m < 32:
        if contador == 8:  # separa o octeto
            maskbin = maskbin + '.'
            contador = 0

        # Verifica se o bit vai ser 0 ou 1
        if m <= int(CIDR - 1):
            maskbin = maskbin + '1'
        else:
            maskbin = maskbin + '0'

        m = m + 1
        contador = contador + 1
    return maskbin


def BinWild(CIDR):
    # calcula a mascara para uma string binaria
    m = 0
    contador = 0
    wildbin = ''  # string de wildcard  binaria

    while m < 32:
        if contador == 8:  # separa o octeto
            wildbin = wildbin + '.'
            contador = 0

        # Verifica se o bit vai ser 0 ou 1
        if m <= int(CIDR - 1):
            wildbin = wildbin + '0'
        else:
            wildbin = wildbin + '1'

        m = m + 1
        contador = contador + 1
    return wildbin


def BinBroad(IP, CIDR):
    return DecBin(Decimal.DecBroadcast(IP, CIDR))


def BinHostMin(IP, CIDR):
    return DecBin(Decimal.DecHostMin(IP, CIDR))


def BinHostMax(IP, CIDR):
    return DecBin(Decimal.DecHostMax(IP, CIDR))


def BinNetwork(IP, CIDR):
    ip = BinIP(IP).split('.')
    mask = BinMask(CIDR).split('.')
    network = ''

    j = 3  # 4 octeto
    while j >= 0:
        # Seleciona o octeto
        tempip = (ip[j])  # transforma um pedaço do octeto em inteiro decimal
        tempmask = (mask[j])  # transforma um pedaço do octeto em inteiro decimal
        i = 7  # 8 bits
        while i >= 0:
            if tempip[i] == '1' and tempmask[i] == '1':
                network = '1' + network
            else:
                network = '0' + network
            i = i - 1
        if j != 0:
            network = '.' + network  # string armazenadora
        j = j - 1
    return network
