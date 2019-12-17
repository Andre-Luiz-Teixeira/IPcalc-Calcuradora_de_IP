import Binarios
import Decimal

IP = input('Digite um IP: ')
CIDR = int(input('Digite o cidr que desja usar: '))

MaskDec = Decimal.DecMask(CIDR)
WildDec = Decimal.DecWild(CIDR)

NetworkDec = Decimal.DecNetWork(IP, CIDR)
BroadDec = Decimal.DecBroadcast(IP, CIDR)
HostMin = Decimal.DecHostMin(IP, CIDR)
HostMax = Decimal.DecHostMax(IP, CIDR)
NumHost = Decimal.DecNumHost(CIDR)

print('\n\n\t\t  -=-=-=-=-=-=-= Decimal =-=-=-=-=-=-')
print('Address\t : ' + IP)
print('Netmask\t : ' + MaskDec)
print('Wildcard : ' + WildDec)

print()
print('Network\t : ' + NetworkDec)
print('Broadcast: ' + BroadDec)
print('HostMin\t : ' + HostMin)
print('HostMax\t : ' + HostMax)
print('Hosts/Net: ' + NumHost)

AddBin = Binarios.BinIP(IP)
MaskBin = Binarios.BinMask(CIDR)
WildBin = Binarios.BinWild(CIDR)

NetworkBin = Binarios.BinNetwork(IP, CIDR)
BroadBin = Binarios.BinBroad(IP, CIDR)
HostMin = Binarios.BinHostMin(IP, CIDR)
HostMax = Binarios.BinHostMax(IP, CIDR)

print('\n\n\t\t  -=-=-=-=-=-=-= Binarios =-=-=-=-=-=-')
print('Address\t : ' + AddBin)
print('Netmask\t : ' + MaskBin)
print('Wildcard : ' + WildBin)

print()
print('Network\t : ' + NetworkBin)
print('Broadcast: ' + BroadBin)
print('HostMin\t : ' + HostMin)
print('HostMax\t : ' + HostMax)
