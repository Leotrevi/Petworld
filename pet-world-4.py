import random

gelo = 9
fogo = 8
trovao = 8
acido = 5
raio = 7
agua = 5
grama = 3
sombra = 2
lama = 1

#--------Arrays--------
#Pets = [0nome, 1vida, 2nivel, 3experiencia, 4Golpe1, 5Golpe2, 6Texto do Golpe, 7Texto do Golpe2]
blits = ["Blits",40,0,0,raio,agua,"raio","agua"]
res = ["Res",40,0,0,lama,grama,"lama","grama"]
cardolv = ["Cardolv",40,0,0,sombra,lama,"sombra","acido"]
byray = ["Byray",40,2,0,trovao, gelo,"trovao","gelo"]

todos_pets = [blits,res,cardolv,byray]
banco_pet = []
meus_pets = [blits]

#-------dados do player
gold = 10
Petbola = 2
pocao = 0
bolsa = [gold,meus_pets,Petbola,pocao]
#----------------
#Vamos usar uma variavel como contador para limitar em até 5 pets que pode levar no bolso
qtd_maxima_pets_na_bolsa = 1

fimdejogo = False

aleatorio = random.randint(0, 3) #de 0 a 2

    
def comprar():
    while True:
        
        print("-----------\nBem vindo a loja de itens\n Você tem",bolsa[0],"de gold")
        item = input("Os itens disponiveis para compra são:\nPetbola(5 gold)\nPocao(10 gold)\nPara sair digite: sair\nO que deseja comprar? ")
        if item == "Petbola" and bolsa[0] >= 5:
            bolsa[2] += 1
            bolsa[0] -= 5
            print("-----------\n1x Petbola comprado\nVocê tem",bolsa[0],"de gold")
            
            
        elif(item == "Pocao" and bolsa[0] >= 10):
            bolsa[3] += 1
            bolsa[0] -= 10
            print("-----------\n1x Pocao comprado (Ela recupera 10 pontos de vida)\nVocê tem",bolsa[0],"de gold")
        
        elif(item == "sair"):
            break
        else:
            print("Gold Insuficiente\n")
    
def bancopet():
    while True:
        opcao_banco = input("Computador ligado,\nDigite a opção desejada:\ndepositar pet\nsacar pet\nsair\n")
        if(opcao_banco == "sair"):
            break
        
        elif(opcao_banco == "depositar pet"):
            if(qtd_maxima_pets_na_bolsa <= 1):
                print(">>>Você deve ter pelo menos 1 pet na sua bolsa!") 
                break
            else:
                print("Seus Pets na sua bolsa:\n",meus_pets)
                posicao = int(input("\nPara depositar, digite a posição do pet na sua bolsa\nExemplo:Se for o primeiro digite 0, se for o segundo digite 1...\n"))
                banco_pet.append(meus_pets[posicao])#adicionando o pet no banco
                meus_pets.pop(posicao) #removendo pet da bolsa
                print("Pet Depositado\nPets em sua bolsa:")
                print(meus_pets)
                qtd_maxima_pets_na_bolsa -= 1
            
                        
        elif(opcao_banco == "sacar pet"):
            if(qtd_maxima_pets_na_bolsa >= 5):
                print(">>>Qantidade maxima de pets na bolsa é 5") 
                break
            else:
                print("Seus Pets na sua bolsa:\n",meus_pets)
                print("Seus Pets no banco:\n",banco_pet)
                posicao_banco = int(input("\nPara sacar, digite a posição do pet no banco\nExemplo:Se for o primeiro digite 0, se for o segundo digite 1...\n"))
                meus_pets.append(banco_pet[posicao_banco])#adicionando o pet no banco
                banco_pet.pop(posicao_banco) #removendo pet da bolsa
                print("Pet Sacado\nPets em sua bolsa:")
                print(meus_pets)
                qtd_maxima_pets_na_bolsa += 1    
                

def explorar():
    oponente = todos_pets[aleatorio]
    print("\n-----------------\nVocê explora a floresta e de repente encontra um pet selvagem")
    print("Você encontrou o pet:",oponente[0])
    print("\nSeus pets",meus_pets)
    posicao_batalha = int(input("Escolha um pet para batalha! Digite a posição do pet no banco\nExemplo:Se for o primeiro digite 0, se for o segundo digite 1...\n"))
    petembatalha = meus_pets[posicao_batalha]
    print("\n-----------------\nPet selecionado:",petembatalha,"\n-----------------\n")
    
    while oponente[1] > 0:
        petembatalha[1] = petembatalha[1] - oponente[4]
        print(">>>Pet oponente usou",oponente[6],"e te causou ",oponente[4],"de dano")
        print(">Sua vida",petembatalha[1],"vida do oponente",oponente[1])
        print("-----\nSeus golpes são:\n",petembatalha[6],"\n",petembatalha[7],"\n-----\n")
        escolha = input("Digite o golpe que deseja utilizar: ")
        
        if(escolha == petembatalha[6]):
            oponente[1] = oponente[1] - petembatalha[4]
            print("\n>>>você usou",petembatalha[6],"e causou",petembatalha[4],"de dano no pet opnonente<<<\n")
            
            
        elif(escolha == petembatalha[7]):
            oponente[1] = oponente[1] - petembatalha[5]
            print("\n>>>você usou",petembatalha[7],"e causou",petembatalha[5],"de dano no pet opnonente<<<\n")
            
        else:
            print("Vê digitou algo errado\n")
        
    #repeti o codigo para o adversario usar um golpe diferente desta vez
        petembatalha[1] = petembatalha[1] - oponente[5]
        print(">>>Pet oponente usou",oponente[7],"e te causou ",oponente[4],"de dano")
        print(">Sua vida",petembatalha[1],"vida do oponente",oponente[1])
        print("-----\nSeus golpes são:\n",petembatalha[6],"\n",petembatalha[7])
        escolha = input("Digite o golpe que deseja utilizar: ")
        
        if(escolha == petembatalha[6]):
            oponente[1] = oponente[1] - petembatalha[4]
            print("\n>>>você usou",petembatalha[6],"e causou",petembatalha[4],"de dano no pet oponente<<<\n")
            
            
        elif(escolha == petembatalha[7]):
            oponente[1] = oponente[1] - petembatalha[5]
            print("\n>>>você usou",petembatalha[7],"e causou",petembatalha[5],"de dano no pet opnonente<<<\n")
            
        else:
            print("Vê digitou algo errado\n")
            
    petembatalha2 = petembatalha
    if(petembatalha2[1] <= 0):
        fimdejogo = True

    else:
        print("\n>>>>>Você ganhou +2 de experiencia<<<<<")
        petembatalha2[3] += 2
        if(petembatalha2[3] >= 10):
            petembatalha2[3] = 0
            petembatalha2[2] += 1
            print("Seu pet",petembatalha2[0],"Subiu de nivel.\nNivel atual:",petembatalha2[3])
        if(bolsa[2] <= 0):
            print("Você não possui Petbolas suficiente, compre mais na loja")
            meus_pets[posicao_batalha] = petembatalha2
        else:
                escolha = input("Vocês deseja tentar capturar este Pet? Digite sim ou nao: ")
                if(escolha == "sim"):
                    bolsa[2] -= 1
                    print("Você lançou uma Petbola")
                    tentasorte = random.randint(0, 1)
                    if(tentasorte == 1):
                        print("Você conseguiu capturar o Pet")
                        meus_pets[posicao_batalha] = petembatalha2
                        if(qtd_maxima_pets_na_bolsa >= 5):
                            print("Você atingiu o limite maximo de 5 pets na bolsa,o pet capturado foi transferido para o banco")
                            banco_pet.append(oponente)
                            print(oponente[0],"capturado foi adicionado ao Banco Pet\n")
                            meus_pets[posicao_batalha] = petembatalha2
                        else:
                            meus_pets.append(oponente)
                            meus_pets[posicao_batalha] = petembatalha2
                            qtd_maxima_pets_na_bolsa += 1
                            
                    else:
                        print("O Pet fugiu e você não conseguiu captura-lo, tente novamente outra vez")
                        meus_pets[posicao_batalha] = petembatalha2
                

def curarpet():
    print("Seus Pets na sua bolsa:\n",meus_pets)
    posicao_curar = int(input("\nPara curar, digite a posição do pet na sua bolsa\nExemplo:Se for o primeiro digite 0, se for o segundo digite 1...\n"))
    petparacurar = meus_pets[posicao_curar]
    petparacurar[1] = 40
    print("Vida do",petparacurar[0],"restaurada para 40 de vida")
    meus_pets[posicao_curar] = petparacurar


while True:
    if(fimdejogo == True):
        break
    else:
        opcao = input("Digite uma das seguintes opções: bolsa, explorar, petshop, ajuda :")
        
        if(opcao == "ajuda"):
            print("--------------\nSempre digite a opção \nExplorar: Para procurar um pet selvagem\nPetshop: local com diversas funções\n--------------")
        
        elif(opcao == "petshop"):
            opcao2 = input("\nBem vindo ao Petshop digite uma das opções: comprar, bancopet, curar pet, sair: ")
            if opcao2 == "comprar":
                comprar()
            elif opcao2 == "bancopet":
                bancopet()
                
            elif opcao2 == "curar pet":
                curarpet()
                
            else:
                print("Saindo do Petshop")
                
        elif opcao == "bolsa":
                print("-----------\nSua bolsa contém os seguinte itens:")
                print("Gold:",bolsa[0],"\nSeus Pets:",bolsa[1],"\nPetbolas:",bolsa[2],"\nPocoes:",bolsa[3],"\n-----------\n")
               
        elif(opcao == "explorar"):
            explorar()


#Desenvolvido por Leonardo Luis Mascarenhas



