#Função principal do jogo. Chama a apresentação, o menu principal e suas opções. Não roda nada, pois depende de outras funções.
def jogo():
    while True:
        print('BEM VINDO AO INSPERMON')
        print('Seu objetivo é capturar o máximo de Inspermons possíveis! São 56 espécies diferentes!')
        insperdex = {}
        insperdex_re = {}
        pedra = [2]
        jogar = input('Aperte ENTER para começar!')
        primeiroinspermon(insperdex,insperdex_re)
        exp = [0]*56
        while True:
                a = random.randint(176.0,212.0)
                b = random.randint(16.0,23.0)
                c = random.randint(9.0,16.0)
                ambiente = {'Xarmander':[a, b, c, 0],'Ninetailes':[a, b, c, 0], 'Growlethe':[a, b, c, 0], 'Arcaine':[a, b, c, 0], 'Ponyt':[a, b, c, 0], 'Magma':[a, b, c, 0], 'Molton':[a, b, c, 0] ,'Cyndakil':[a, b, c, 0] ,'Slug':[a, b, c, 0] ,'Magcarg':[a, b, c, 0] ,'Maglay':[a, b, c, 0] ,'Pidju':[a, b, c, 1] ,'Fearrow':[a, b, c, 1] ,'Zubatman':[a, b, c, 1] ,'Farpatch':[a, b, c, 1] ,'Cypher':[a, b, c, 1] ,'Dragonose':[a, b, c, 1] ,'Aerodactilo':[a, b, c, 1] ,'Lediano':[a, b, c, 1] ,'Acrobat':[a, b, c, 1] ,'Xatow':[a, b, c, 1] ,'Raichow':[a, b, c, 1], 'Picaxu':[a, b, c, 2],'Zeraia':[a, b, c, 2], 'Magcamp':[a, b, c, 2] ,'Voltain':[a, b, c, 2] ,'Prototian':[a, b, c, 2] ,'Joulian':[a, b, c, 2] ,'Latent':[a, b, c, 2] ,'Flafy':[a, b, c, 2] ,'Aedunit':[a, b, c, 2] ,'Raike':[a, b, c, 2] ,'Plusty':[a, b, c, 2] ,'Mirion':[a, b, c, 3] ,'Bubussauro':[a, b, c, 3], 'Katerpi':[a, b, c, 3] ,'Bidrill':[a, b, c, 3] ,'Tatata':[a, b, c, 3] ,'Sandshell':[a, b, c, 3] ,'Widol':[a, b, c, 3] ,'Kakunol':[a, b, c, 3] ,'Vivolplume':[a, b, c, 3] ,'Dugtri':[a, b, c, 3] ,'Geodudol':[a, b, c, 3] ,'Dodul':[a, b, c, 4] ,'Giromon':[a, b, c, 4], 'Squirtlow':[a, b, c, 4] ,'Poliswag':[a, b, c, 4] ,'Poliwilly':[a, b, c, 4] ,'Tentacul':[a, b, c, 4] ,'Slowbrow':[a, b, c, 4] ,'Shelter':[a, b, c, 4] ,'Cloybster':[a, b, c, 4] ,'Krabay':[a, b, c, 4] ,'Kingle':[a, b, c, 4]}
                ambiente_re = {'Xarmander':[a, b, c, 0],'Ninetailes':[a, b, c, 0], 'Growlethe':[a, b, c, 0], 'Arcaine':[a, b, c, 0], 'Ponyt':[a, b, c, 0], 'Magma':[a, b, c, 0], 'Molton':[a, b, c, 0] ,'Cyndakil':[a, b, c, 0] ,'Slug':[a, b, c, 0] ,'Magcarg':[a, b, c, 0] ,'Maglay':[a, b, c, 0] ,'Pidju':[a, b, c, 1] ,'Fearrow':[a, b, c, 1] ,'Zubatman':[a, b, c, 1] ,'Farpatch':[a, b, c, 1] ,'Cypher':[a, b, c, 1] ,'Dragonose':[a, b, c, 1] ,'Aerodactilo':[a, b, c, 1] ,'Lediano':[a, b, c, 1] ,'Acrobat':[a, b, c, 1] ,'Xatow':[a, b, c, 1] ,'Raichow':[a, b, c, 1], 'Picaxu':[a, b, c, 2],'Zeraia':[a, b, c, 2], 'Magcamp':[a, b, c, 2] ,'Voltain':[a, b, c, 2] ,'Prototian':[a, b, c, 2] ,'Joulian':[a, b, c, 2] ,'Latent':[a, b, c, 2] ,'Flafy':[a, b, c, 2] ,'Aedunit':[a, b, c, 2] ,'Raike':[a, b, c, 2] ,'Plusty':[a, b, c, 2] ,'Mirion':[a, b, c, 3] ,'Bubussauro':[a, b, c, 3], 'Katerpi':[a, b, c, 3] ,'Bidrill':[a, b, c, 3] ,'Tatata':[a, b, c, 3] ,'Sandshell':[a, b, c, 3] ,'Widol':[a, b, c, 3] ,'Kakunol':[a, b, c, 3] ,'Vivolplume':[a, b, c, 3] ,'Dugtri':[a, b, c, 3] ,'Geodudol':[a, b, c, 3] ,'Dodul':[a, b, c, 4] ,'Giromon':[a, b, c, 4], 'Squirtlow':[a, b, c, 4] ,'Poliswag':[a, b, c, 4] ,'Poliwilly':[a, b, c, 4] ,'Tentacul':[a, b, c, 4] ,'Slowbrow':[a, b, c, 4] ,'Shelter':[a, b, c, 4] ,'Cloybster':[a, b, c, 4] ,'Krabay':[a, b, c, 4] ,'Kingle':[a, b, c, 4]}
                inspermon = []
                inspermon_am = []
                dados_am = []
                chaves = insperdex.keys()
                for i in chaves:
                    inspermon.append(i)
                chaves = ambiente.keys()
                for i in chaves:
                    inspermon_am.append(i)
                valores = ambiente.values()
                for d in valores:
                    dados_am.append(d)
                valores = ambiente.values()
                opcao = input('O que deseja fazer?(Digite a letra)\n(a)Passear\n(b)Recuperar Inspermons (é necessário possuir Pedras Preciosas para tal)\n(c)Acessar Insperdex\n(d)Dormir\n(e)Recomeçar\n:')
                if opcao == 'a':
                    lugares(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,insperdex,insperdex_re,pedra,exp)
                if opcao == 'c':
                    F1 = []
                    F2 = []
                    Ar1 = []
                    Ar2 = []
                    R1 = []
                    R2 = []
                    T1 = []
                    T2 = []
                    Ag1 = []
                    Ag2 = []
                    for x in insperdex:
                        if insperdex[x][3] == 0 and insperdex[x][0] == insperdex_re[x][0]:
                            F1.append(x)
                        elif insperdex[x][3] == 0 and insperdex[x][0] != insperdex_re[x][0]:
                            F2.append(x)
                        elif insperdex[x][3] == 1 and insperdex[x][0] == insperdex_re[x][0]:
                            Ar1.append(x)
                        elif insperdex[x][3] == 1 and insperdex[x][0] != insperdex_re[x][0]:
                            Ar2.append(x)
                        elif insperdex[x][3] == 2 and insperdex[x][0] == insperdex_re[x][0]:
                            R1.append(x)
                        elif insperdex[x][3] == 2 and insperdex[x][0] != insperdex_re[x][0]:
                            R2.append(x)
                        elif insperdex[x][3] == 3 and insperdex[x][0] == insperdex_re[x][0]:
                            T1.append(x)
                        elif insperdex[x][3] == 3 and insperdex[x][0] != insperdex_re[x][0]:
                            T2.append(x)
                        elif insperdex[x][3] == 4 and insperdex[x][0] == insperdex_re[x][0]:
                            Ag1.append(x)
                        elif insperdex[x][3] == 4 and insperdex[x][0] != insperdex_re[x][0]:
                            Ag2.append(x)
                    while True:
                        print('Seu Insperdex: (Dica: os Inspermons da esquerda estão totalmente saudáveis. Os da direita estão feridos)\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
                        atributos = input('Deseja ver os atributos de um Inspermon do Insperdex?   (Digite a Letra)\n(a)Sim\n(b)Não\n:')
                        if atributos == 'a':
                            while True:
                                print('Seu Insperdex: (Dica: os Inspermons da esquerda estão totalmente saudáveis. Os da direita estão feridos):\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
                                nome = input('Digite o nome do Inspermon\n:')
                                if nome in inspermon:
                                    mostrainspermon(nome,insperdex,exp,inspermon)
                                    break
                        if atributos == 'b':
                            break
                if opcao == 'b':
                    if pedra[0] == 1:
                        print('Você possui 1 Pedra Preciosa')
                    elif pedra[0] != 1:
                        print('Você possui {} Pedras Preciosas'.format(pedra[0]))
                    F1 = []
                    F2 = []
                    Ar1 = []
                    Ar2 = []
                    R1 = []
                    R2 = []
                    T1 = []
                    T2 = []
                    Ag1 = []
                    Ag2 = []
                    for x in insperdex:
                        if insperdex[x][3] == 0 and insperdex[x][0] == insperdex_re[x][0]:
                            F1.append(x)
                        elif insperdex[x][3] == 0 and insperdex[x][0] != insperdex_re[x][0]:
                            F2.append(x)
                        elif insperdex[x][3] == 1 and insperdex[x][0] == insperdex_re[x][0]:
                            Ar1.append(x)
                        elif insperdex[x][3] == 1 and insperdex[x][0] != insperdex_re[x][0]:
                            Ar2.append(x)
                        elif insperdex[x][3] == 2 and insperdex[x][0] == insperdex_re[x][0]:
                            R1.append(x)
                        elif insperdex[x][3] == 2 and insperdex[x][0] != insperdex_re[x][0]:
                            R2.append(x)
                        elif insperdex[x][3] == 3 and insperdex[x][0] == insperdex_re[x][0]:
                            T1.append(x)
                        elif insperdex[x][3] == 3 and insperdex[x][0] != insperdex_re[x][0]:
                            T2.append(x)
                        elif insperdex[x][3] == 4 and insperdex[x][0] == insperdex_re[x][0]:
                            Ag1.append(x)
                        elif insperdex[x][3] == 4 and insperdex[x][0] != insperdex_re[x][0]:
                            Ag2.append(x)
                    if len(insperdex) == 1:
                        print('Você possui 1 Inspermon')
                        if pedra[0] >= 1:
                            while True:
                                print('Seu Insperdex: (Dica: os Inspermons da esquerda estão totalmente saudáveis. Os da direita estão feridos)\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
                                recuperar = input('Deseja recuperar os seus Inspermons? (tal ação custará uma Pedra Preciosa)  (Digite a Letra)\n(a)Sim\n(b)Não\n:')
                                if recuperar == 'a':
                                    print('Seus Inspermons foram recuperados com sucesso!')
                                    pedra[0] = pedra[0] - 1
                                    for x in insperdex:
                                        insperdex[x] = insperdex_re[x][:]
                                    break
                                if recuperar == 'b':
                                    break
                        else:
                            print('Você não possui Pedras Preciosas suficientes')  
                    elif len(insperdex) > 1:
                        print('Você possui {} Inspermons'.format(len(insperdex)))
                        if len(insperdex) == 2:
                            print('custo de recuperação:  pedra')
                        elif len(insperdex) > 3:
                            print('custo de recuperação: {} pedras'.format(len(insperdex)//2))
                        if pedra[0] >= len(insperdex)//2:
                            while True:
                                print('Seu Insperdex: (Dica: os Inspermons da esquerda estão totalmente saudáveis. Os da direita estão feridos)\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
                                recuperar = input('Deseja recuperar os seus Inspermons? (Digite a Letra)\n(a)Sim\n(b)Não\n:')
                                if recuperar == 'a':
                                    print('Seus Inspermons foram recuperados com sucesso!')
                                    pedra[0] = pedra[0] - (len(insperdex)//2)
                                    for x in insperdex:
                                        insperdex[x] = insperdex_re[x][:]
                                    break
                                if recuperar == 'b':
                                    break
                        else:
                            print('Você não possui Pedras Preciosas suficientes')
                if opcao == 'd':
                    print('Ok, até mais tarde')
                    return
                if opcao == 'e':
                    print('BOA SORTE')
                    break
                if insperdex == {}:
                    print('VOCÊ PERDEU')
                    break
                if len(insperdex) == 56:
                    print('VOCÊ GANHOU ')
                    ganhou = input('O que deseja fazer? (Digite a Letra)\n(a)Continuar\n(b)Recomeçar\n:')
                    if ganhou == 'a':
                        print('Novo Inspermon adquirido! MegaBlast foi adicionado ao Insperdex ')
                        insperdex['MegaBlast'] = [10000,50,16,0]
                        insperdex_re['MegaBlast'] = [10000,50,16,0]
                    if ganhou == 'b':
                        break
        if jogar == 'b':
            print('Ok, até mais tarde!')
            return

#Essas funções servem para o jogador escolher o Inspermon com que deseja começar o jogo. São três opções: Xarmander, Bubussauro e Squirtlow 
def primeiroinspermon(insperdex,insperdex_re):
    print(' ')
    print('ESCOLHA DO PRIMEIRO INSPERMON')
    print(' ')
    mostrainspermoninicial('Xarmander')
    print(' ')
    mostrainspermoninicial('Bubussauro')
    print(' ')
    mostrainspermoninicial('Squirtlow')
    print(' ')
    while True:
        primeiroinspermon = input('Escolha o seu primeiro Inspermon (Digite a Letra)\n(a)Xarmander\n(b)Bubussauro\n(c)Squirtlow\n:')
        if primeiroinspermon == 'a' or primeiroinspermon == 'A':
            insperdex['Xarmander'] = insperdex0['Xarmander'][:]
            insperdex_re['Xarmander'] = insperdex0['Xarmander'][:]
            return
        if primeiroinspermon == 'b' or primeiroinspermon == 'B':
            insperdex['Bubussauro'] = insperdex0['Bubussauro'][:]
            insperdex_re['Bubussauro'] = insperdex0['Bubussauro'][:]
            return
        if primeiroinspermon == 'c' or primeiroinspermon == 'C':
            insperdex['Squirtlow'] = insperdex0['Squirtlow'][:]
            insperdex_re['Squirtlow'] = insperdex0['Squirtlow'][:]
            return
def mostrainspermoninicial(nome):
    print('Inspermon:{}'.format(nome))
    print('Vida:{}'.format(insperdex0[nome][0]))
    print('Poder:{}'.format(insperdex0[nome][1]))
    print('Defesa:{}'.format(insperdex0[nome][2]))
    print('Elemento:{}'.format(elementos[insperdex0[nome][3]]))

import random
insperdex0 = {'Xarmander':[200, 22, 12, 0], 'Bubussauro':[200, 21, 13, 3], 'Squirtlow':[200, 20, 14, 4]}
elementos = ['Fogo','Ar','Raio','Terra','Água']
ciclo = [['Fogo','Ar'],['Ar','Raio'],['Raio','Terra'],['Terra','Água'],['Água','Fogo']]


jogo()

