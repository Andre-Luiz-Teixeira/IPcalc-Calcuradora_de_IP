import Binarios


def DecMask(CIDR):
    return binDec(Binarios.BinMask(CIDR))


def DecNumHost(CIDR):
    CIDR = ((2 ** (32 - int(CIDR))) - 2)
    return str(CIDR)


def DecWild(CIDR):
    return binDec(Binarios.BinWild(CIDR))


def DecBroadcast(IP, CIDR):
    OctIP = DecNetWork(IP, CIDR).split('.')
    wild = DecWild(CIDR).split('.')
    Broad = ''
    i = 3

    while i >= 0:
        Broadcast = int(OctIP[i]) + int(wild[i])
        Broad = str(Broadcast) + Broad
        i = i - 1
        if i != -1:
            Broad = '.' + Broad  # string armazenadora

    return Broad


def DecHostMax(IP, CIDR):
    Max = DecBroadcast(IP, CIDR).split('.')
    Max[3] = int(Max[3]) - 1
    return '.'.join(map(str, Max))


def DecHostMin(IP, CIDR):
    Min = DecNetWork(IP, CIDR).split('.')
    Min[3] = int(Min[3]) + 1
    return '.'.join(map(str, Min))


def DecNetWork(IP, CIDR):
    return binDec(Binarios.BinNetwork(IP, CIDR))


def binDec(binario):
    Bin = binario.split('.')
    j = 3  # 4 octeto
    decimal = ''
    while j >= 0:
        # Seleciona o octeto
        temp = (Bin[j])  # transforma um pedaço do octeto em inteiro decimal
        i = 7  # 8 bits
        local = 0
        soma = 0
        while i >= 0:
            bit = int(temp[i])
            if bit == 1:
                soma = (2 ** local) + soma
            i = i - 1
            local = local + 1

        decimal = str(soma) + decimal
        if j != 0:
            decimal = '.' + decimal  # string armazenadora
        j = j - 1
    return decimal
