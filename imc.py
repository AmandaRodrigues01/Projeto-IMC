#Abaixo de 17	Muito abaixo do peso
#Entre 17 e 18,49	Abaixo do peso
#Entre 18,5 e 24,99	Peso normal
#Entre 25 e 29,99	Acima do peso
#Entre 30 e 34,99	Obesidade I
#Entre 35 e 39,99	Obesidade II (severa)
#Acima de 40	Obesidade III (mórbida)

lista = []
pessoas = dict()
while True:
    pessoas.clear()
    pessoas['nome']=(str(input('digite seu nome:')))
   
    pessoas['idade']=(int(input('sua idade:')))
    
    pessoas['peso']=(float(input('Peso:kg')))
    pessoas['altura']=(float(input('digite sua altura:(m)')))
    pessoas['imc']= pessoas['peso'] // (pessoas['altura'] ** 2 )
    
    lista.append(pessoas.copy())

    continuar = str(input('Quer continuar?[s/n]'))

    if continuar == 'n':
        break
for p in lista:
    if  p['imc'] <17:
        print
        print(f'A pessoas {p["nome"]} ESTÃO MUITO ABAIXO DO PESO')

    if p['imc']  <= 18.99  ==17:
        print(f'A pessoas {p["nome"]} ESTAO ABAIXO DO PESO')
   
    if p['imc'] <= 24.99   >= 18.5:
            print(F'A pessoas  {p["nome"]} está no PESO NORMAL')
    if p['imc'] <=29.99  ==25: 
        print(f'A pessoas {p["nome"]} está ACIMA DO PESO')
    if p['imc'] <= 34.99 == 30: 
        print(f'As pessas{p["nome"]} está EM OBESIDADE I')  
    if p['imc'] <= 39.99 ==35 : 
        print(f'As pessoas {p["nome"]} ESTÃO EM OBESIDADE II(SEVERA)')  

    if p['imc'] > 40:
        print()
        print(f'As pessoas {p["nome"]} está EM OBESIDADE MORBIDA')
#print(lista)
