import math

def verFloat(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = float(n)
            ok = True
        else:
            print('ERR0! Digite um número válido')
        if ok:
            break
    return valor

stp = '1'
print('---------------------------------------------------\n',
      '  PROGRAMA DE MEDIÇÃO CO2 PARA EMPRESAS DE VIAÇÃO\n '
      f'---------------------------------------------------')
while (stp == '1'):

    lmt = verFloat('Qual limite de emissão de CO2 de sua empresa em KG? \n ')

    onibusD = verFloat('Quantos ônibus a Diesel foram às ruas durantes o ano?: \n')
    kmD = verFloat('Quantos Kilometros os ônibus a Diesel percorreram durante o ano?: \n')
    onibusE = verFloat('Quantos ônibus a Etanol foram às ruas durantes o ano?: \n')
    kmE = verFloat('Quantos Kilometros os ônibus a Etanol percorreram durante o ano?: \n ')

    tKgDi = (kmD * 2.6) #litro de diesel = 2.6kg CO2
    tKgEt = (kmE * 1.8) #litro de etanol = 1.8kg CO2

    vlmt = tKgDi+tKgEt # soma / verificar limite
    res = (tKgDi * 2) -  (tKgDi - tKgEt) #deixamos de gerar
    exc = vlmt #excedido
    crt = (vlmt/1000)  #credito





    if exc > lmt:
        print(f'Sua empresa excedeu o limite de Co2 totalizando {round((vlmt/1000),2)} Toneladas de Co2. Neste caso, é necessário plantar {math.ceil((exc/1000)*7)} árvores para compensar.')


    else:
        print(f'Sua empresa gerou {round((vlmt/1000),2)} Toneladas de Co2 mas está dentro do limite! \n ')
        print(f'Vocês deixaram de emitir {round((res/1000),2)} Toneladas de Co2, totalizando {math.floor(crt)} créditos')
        lcr = crt*75 #lucro se vender o crédito, valor de cada crédito = R$ 75,00 no mercado de carbono.
        print(f'A empresa pode lucrar R$ {round(lcr,2)} se vender os créditos')
                

    stp = input("\nDigite 1 para repetir ou qualquer número para sair : ")
if (stp != '1'):
    print('Terminamos!')
