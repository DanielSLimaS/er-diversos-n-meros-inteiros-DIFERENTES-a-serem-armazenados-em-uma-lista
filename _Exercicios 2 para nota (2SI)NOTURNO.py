#Exercicios 2 para nota (2SI)NOTURNO

#SALA 3
def cadastronum ():
    lista = []
    while True:
        x = int(input("Digite um número: "))
        #SAIR DO LOOP QUANDO FOR 0
        if(x==0):
            print("Saindo...")
            break
        #VALIDAR SE O NUMERO ESTA NA LISTA 
        if (validaSeONumeroEstaNaLista(x,lista)):
            print("O numero ",x,"já está na lista!")
            print("Digite outro número")
        else:
            lista.append(x)
    return lista
#CONVERTER OS VALORES PARA POSITIVO
def validarNegativo(lista):
    for i in lista:
        if(i<0):
        #Todo NUMERO NEGATIVO MULTIPLICADO POR NEGATIVO FICA POSITIVO
            i = i * (-1)
        listaSemNegativo.append(i)
    return listaSemNegativo

def contaDigito(listaSemNegativo):
    sTexto = ""
    #concatenar a lista em uma variavel string
    for i in listaSemNegativo:
        sTexto +=str(i)
    return (sTexto,len(sTexto))

def validaSeONumeroEstaNaLista(x,lista):
    # if (x in lista):
    #     return True
    # else:
    #     return False
    #OUTRA MANEIRA DE VALIDAR
    temNalista = False
    for i in lista:
        if(x==i):
            temNalista = True
    return temNalista

#MAIN()

#declarações de variaveis
sTexto =  ""
lista = []
listaSemNegativo = []
qtdDigito = 0 
#chamando as funções
lista = cadastronum()
listaSemNegativo = validarNegativo(lista)
sTexto,qtdDigito= contaDigito(listaSemNegativo)

#EXIBIR VALORES
#lista padrao
if(len(lista)>0):
    print('lista padrão')
    print(lista)
    #lista sem negativo
    print('Lista sem negativo')
    print(listaSemNegativo)
    #contaDigito
    print("Numeros impressos um ao lado do outro: ", sTexto)
    print("Quantidade de digitos:",qtdDigito )
else:
    print("Lista Vazia!")
