# BEM VINDO AO INSPERMON
# O objetivo do jogo é capturar todos os Inspermons de campo, além dos especiais.

#Abre as opções de escolha de Inspermon inicial
def mostrainspermoninicial(nome):
    print('Inspermon:{}'.format(nome))
    print('Vida:{}'.format(insperdex0[nome][0]))
    print('Poder:{}'.format(insperdex0[nome][1]))
    print('Defesa:{}'.format(insperdex0[nome][2]))
    print('Elemento:{}'.format(elementos[insperdex0[nome][3]]))

#Mostra os Inspermons no Insperdex
def mostrainspermon(nome,insperdex,exp,inspermon):
    print('Inspermon:{}'.format(nome))
    print('Vida:{}'.format(insperdex[nome][0]))
    print('Poder:{}'.format(insperdex[nome][1]))
    print('Defesa:{}'.format(insperdex[nome][2]))
    print('Elemento:{}'.format(elementos[insperdex[nome][3]]))
    print('Possui {} xp, faltam {} xp para evolução'.format(exp[inspermon.index(nome)]%100,100 - exp[inspermon.index(nome)]%100))

#Mostra os Inspermons selvagens
def mostrainspermon_am(r,ambiente,inspermon_am):
    print('Inspermon:{}'.format(inspermon_am[r]))
    print('Vida:{}'.format(ambiente[inspermon_am[r]][0]))
    print('Poder:{}'.format(ambiente[inspermon_am[r]][1]))
    print('Defesa:{}'.format(ambiente[inspermon_am[r]][2]))
    print('Elemento:{}'.format(elementos[ambiente[inspermon_am[r]][3]]))

import random

insperdex0 = {'Xarmander':[200, 22, 12, 0], 'Bubussauro':[200, 21, 13, 3], 'Squirtlow':[200, 20, 14, 4]}
#Cada Inspermon tem um determinado elemento
elementos = ['Fogo','Ar','Raio','Terra','Água']
#Os elementos interagem entre si. Todos os elementos tem vantagem contra algum outro, da seguinte forma:
#Fogo > Ar
#Ar > Raio
#Raio > Terra
#Terra > Água
#Água > Fogociclo = [['Fogo','Ar'],['Ar','Raio'],['Raio','Terra'],['Terra','Água'],['Água','Fogo']]
ciclo = [['Fogo','Ar'],['Ar','Raio'],['Raio','Terra'],['Terra','Água'],['Água','Fogo']]

#A função abaixo mostra o menu do jogo.
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
                if opcao == 'b':
                    #Pedras Preciosas servem para curar os Inspermons. São adquiridas em combate.
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
                        print(' ')
                        print('Você possui 1 Inspermon')
                        if pedra[0] >= 1:
                            while True:
                                print('Seu Insperdex: (Dica: os Inspermons da esquerda estão totalmente saudáveis. Os da direita estão feridos)\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
                                print(' ')
                                recuperar = input('Deseja recuperar os seus Inspermons? (tal ação custará Pedras Preciosas)  (Digite a Letra)\n(a)Sim\n(b)Não\n:')
                                if recuperar == 'a':
                                    print(' ')
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
                            print(' ')
                            print('Custo de recuperação: 1 Pedra')
                            print(' ')
                        elif len(insperdex) > 3:
                            print('Custo de recuperação: {} Pedras'.format(len(insperdex)//2))
                        if pedra[0] >= len(insperdex)//2:
                            while True:
                                print('Seu Insperdex: (Dica: os Inspermons da esquerda estão totalmente saudáveis. Os da direita estão feridos)\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
                                recuperar = input('Deseja recuperar os seus Inspermons? (Digite a Letra)\n(a)Sim\n(b)Não\n:')
                                if recuperar == 'a':
                                    print(' ')
                                    print('Seus Inspermons foram recuperados com sucesso!')
                                    print(' ')
                                    pedra[0] = pedra[0] - (len(insperdex)//2)
                                    for x in insperdex:
                                        insperdex[x] = insperdex_re[x][:]
                                    break
                                if recuperar == 'b':
                                    break
                        else:
                            print(' ')
                            print('Você não possui Pedras Preciosas suficientes')
                            print(' ')
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
                if opcao == 'd':
                    print('Ok, até mais tarde')
                    return
                if opcao == 'e':
                    print(' ')
                    print('OK, REINICIANDO')
                    print(' ')
                    print(' ')
                    print(' ')
                    print(' ')
                    break
                if insperdex == {}:
                    #Você perde o jogo ao perder todos os Inspermons
                    print('VOCÊ PERDEU')
                    return
                #Inspermons especiais são adquiridos conforme o jogador captura Inspermons. São eles: Ghostbul, Supertooth, Thundercrick e MegaBlast
                if len(insperdex) == 10:
                    print(' ')
                    print('Novo Inspermon adquirido! Ghostbul foi adicionado ao Insperdex')
                    insperdex['Ghostbul'] = [225,25,16,1]
                    insperdex_re['Ghostbul'] = [225,25,16,1]
                if len(insperdex) == 25:
                    print(' ')
                    print('Novo Inspermon adquirido! Supertooth foi adicionado ao Insperdex')
                    insperdex['Supertooth'] = [250,15,15,3]
                    insperdex_re['Supertooth'] = [250,15,15,3]
                if len(insperdex) == 40:
                    print(' ')
                    print('Novo Inspermon adquirido! Thundercrick foi adicionado ao Insperdex')
                    insperdex['Thundercrick'] = [215,35,15,3]
                    insperdex_re['Thundercrick'] = [215,35,15,3]     
                if len(insperdex) == 56:
                    print(' ')
                    print('VOCÊ GANHOU!!')
                    print('Novo Inspermon adquirido! MegaBlast foi adicionado ao Insperdex ')
                    insperdex['MegaBlast'] = [10000,50,16,0]
                    insperdex_re['MegaBlast'] = [10000,50,16,0]
                    print(' ')
                    ganhou = input('O que deseja fazer? (Digite a Letra)\n(a)Continuar\n(b)Recomeçar\n:')
                    if ganhou == 'a':
                        continue
                    if ganhou == 'b':
                        break
        if jogar == 'b':
            print('Ok, até mais tarde!')
            return

#Função que mostra as três opções de primeiro Inspermon.
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
def lugares(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,insperdex,insperdex_re,pedra,exp):
    escolha = input('Para onde deseja ir?   (Digite a letra)\n(a)Ir para a Floresta dos Elementos (Elementos: Terra, Água, Fogo, Ar e Raio) \n(b)Ir para o Deserto dos Ventos Cortantes (Elementos: Fogo e Ar)\n(c)Ir para a Praia Rochosa (Elementos: Terra e Água)\n(d)Ir para as Montanhas Trovoantes (Elementos: Raio e Terra)\n(e)Ir para as Planícies Tempestuosas (Elementos: Ar e Raio)\n:')
    if escolha == 'a' or escolha == 'A':
        while True:
            r = random.randint(0,len(inspermon_am)-1)
            if elementos[ambiente[inspermon_am[r]][3]] in ['Terra', 'Água', 'Fogo', 'Ar', 'Raio']:
                l = lutar(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,r,insperdex,insperdex_re,pedra,exp)
                return
    if escolha == 'b' or escolha == 'B':
        while True:
            r = random.randint(0,len(inspermon_am)-1)
            if elementos[ambiente[inspermon_am[r]][3]] in ['Fogo', 'Ar']:
                l = lutar(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,r,insperdex,insperdex_re,pedra,exp)
                return
    if escolha == 'c' or escolha == 'C':
        while True:
            r = random.randint(0,len(inspermon_am)-1)
            if elementos[ambiente[inspermon_am[r]][3]] in ['Terra', 'Água']:
                l = lutar(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,r,insperdex,insperdex_re,pedra,exp)
                return
    if escolha == 'd' or escolha == 'D':
        while True:
            r = random.randint(0,len(inspermon_am)-1)
            if elementos[ambiente[inspermon_am[r]][3]] in ['Raio', 'Terra']:
                l = lutar(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,r,insperdex,insperdex_re,pedra,exp)
                return
    if escolha == 'e' or escolha == 'E':
        while True:
            r = random.randint(0,len(inspermon_am)-1)
            if elementos[ambiente[inspermon_am[r]][3]] in ['Ar', 'Raio']:
                l = lutar(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,r,insperdex,insperdex_re,pedra,exp)
                return

#Função do menu de luta. É possível escolher o Inspermon para lutar, acessar os atributos no Insperdex ou fugir.
#As chances de fuga bem sucedida são de 60%.
def lutar(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,r,insperdex,insperdex_re,pedra,exp):
    print(' ')
    print(' ')
    print('VOCÊ ENCONTROU UM INSPERMON SELVAGEM!')
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
        print(' ')
        mostrainspermon_am(r,ambiente,inspermon_am)
        print(' ')
        print('Seu Insperdex: (Dica: os Inspermons da esquerda estão totalmente saudáveis. Os da direita estão feridos)\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
        print(' ')
        atributos = input('Deseja acessar os atributos de seus Inspermons? (Digite a Letra)\n(a)Sim\n(b)Não\n:')
        if atributos == 'a':
            nome = input('Digite o nome do Inspermon\n:')
            if nome in inspermon:
                mostrainspermon(nome,insperdex,exp,inspermon)
                continue
        if atributos == 'b':
            lutar = input('O que deseja fazer?   (Digite a letra)\n(a)Lutar\n(b)Fugir\n:')
            if lutar == 'a':
                while True:
                    print('Seu Insperdex:   (Os da esquerda possuem vida cheia)\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
                    i = input('Escolha seu Inspermon para lutar   (Digite o nome do Inspermon)\n:')
                    if i in inspermon:
                        if [elementos[ambiente[inspermon_am[r]][3]],elementos[insperdex[i][3]]] in ciclo:
                            batalha(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,i,insperdex[i],r,0,0.2,0,insperdex,insperdex_re,pedra,exp)
                            return 
                        if [elementos[insperdex[i][3]],elementos[ambiente[inspermon_am[r]][3]]] in ciclo:
                            batalha(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,i,insperdex[i],r,0.2,0,0,insperdex,insperdex_re,pedra,exp)
                            return 
                        else:
                            batalha(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,i,insperdex[i],r,0,0,0,insperdex,insperdex_re,pedra,exp)
                            return 
            if lutar == 'b':
                fugir = random.randint(1,5)
                if fugir <= 3:
                    print(' ')
                    print('Você conseguiu fugir!')
                    print(' ')
                    return
                else:
                    print(' ') 
                    print('Você não conseguiu fugir!')
                    print(' ')
                    while True:
                        mostrainspermon_am(r,ambiente,inspermon_am)
                        print('Seu Insperdex:(Vida maior ou igual a 100 a esquerda, vida menor que 100 a direita)\nFogo:{},{}\nAr:{},{}\nRaio:{},{}\nTerra:{},{}\nÁgua:{},{}'.format(F1,F2,Ar1,Ar2,R1,R2,T1,T2,Ag1,Ag2))
                        i = input('Escolha seu Inspermon   (Digite o nome do Inspermon)\n:')
                        if i in inspermon:
                            if [elementos[ambiente[inspermon_am[r]][3]],elementos[insperdex[i][3]]] in ciclo:
                                batalha(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,i,insperdex[i],r,0,0.2,1,insperdex,insperdex_re,pedra,exp)
                                return 
                            if [elementos[insperdex[i][3]],elementos[ambiente[inspermon_am[r]][3]]] in ciclo:
                                batalha(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,i,insperdex[i],r,0.2,0,1,insperdex,insperdex_re,pedra,exp)
                                return 
                            else:
                                batalha(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,i,insperdex[i],r,0,0,1,insperdex,insperdex_re,pedra,exp)
                                return

#Função de batalha. Os Critical Hits são aleatórios. Além disso, o combate conta com bônus elementais.
#A cada vitória, o Inspermon ganhador obtém 25 xp.
def batalha(ambiente,ambiente_re,inspermon,inspermon_am,dados_am,i,x,r,a,b,o,insperdex,insperdex_re,pedra,exp):
    sj = 0
    so = 0
    while True:
        s = random.randint(1,82)
        if o != 0:
            vidajogador = x[0]-(dados_am[r][1]*(1+b)-x[2])
            if s == 1 :
                vidajogador = vidajogador - 40
                print('Você recebeu Critical Hit: 40')
            elif s > 1 and s <= 3:
                vidajogador = vidajogador - 30
                print('Você recebeu Critical Hit: 30')
            elif s > 3 and s <= 8:
                vidajogador = vidajogador - 20
                print('Você recebeu Critical Hit: 20')
            elif s > 8 and s <= 18:
                vidajogador = vidajogador - 10
                print('Você recebeu Critical Hit: 10')
            x[0] = vidajogador
            so = so + dados_am[r][1]*b
            if vidajogador <= 0:
                if a == 0 and b == 0:
                    print('Resultado:{}/{}'.format(vidajogador,vidaoponente))
                    print('Você perdeu o seu Inspermon!')
                    del insperdex[i]
                    del insperdex_re[i]
                    return
                if a == 0.2 and b == 0:
                    print('Seu inimigo perdeu {} de vida por dano de elemento'.format(sj))
                    print('Resultado:{}/{}'.format(vidajogador,vidaoponente))
                    print(' ')
                    print('Você perdeu o seu Inspermon!')
                    del insperdex[i]
                    del insperdex_re[i]
                    return
                if a == 0 and b == 0.2:
                    print('Você perdeu {} de vida por dano de elemento'.format(so))
                    print('Resultado:{}/{}'.format(vidajogador,vidaoponente))
                    print(' ')
                    print('Você perdeu o seu Inspermon!')
                    del insperdex[i]
                    del insperdex_re[i]
                    return
        vidaoponente = dados_am[r][0]-(x[1]*(1+a)-dados_am[r][2])
        if s > 64 and s <= 74:
            vidaoponente = vidaoponente - 10
            print('Seu inimigo recebeu Critical Hit: 10')
        elif s > 74 and s <= 79:
            vidaoponente = vidaoponente - 20
            print('Seu inimigo recebeu Critical Hit: 20')
        elif s > 79 and s <= 81:
            vidaoponente = vidaoponente - 30
            print('Seu inimigo recebeu Critical Hit: 30')
        elif s == 82:
            vidaoponente = vidaoponente - 40
            print('Seu inimigo recebeu Critical Hit: 40')
        dados_am[r][0] = vidaoponente
        sj = sj + x[1]*a
        if vidaoponente <= 0:
            if a == 0 and b == 0:
                print(' ')
                print('Você ganhou 25 xp')
                exp[inspermon.index(i)] = exp[inspermon.index(i)] + 25
                if exp[inspermon.index(i)]%100 == 0:
                    insperdex_re[i][0] = insperdex_re[i][0]*(1.05)
                    insperdex_re[i][1] = insperdex_re[i][1]*(1.03)
                    insperdex[i][0] = insperdex_re[i][0]
                    insperdex[i][1] = insperdex_re[i][1]
                capturar(i,r,inspermon_am,ambiente_re,insperdex,insperdex_re,pedra)
                return
            if a == 0.2 and b == 0:
                print('Seu inimigo perdeu {} de vida por dano de elemento!'.format(sj))
                print('Resultado:{}/{}'.format(vidajogador,vidaoponente))
                print('Você ganhou 25 xp')
                exp[inspermon.index(i)] = exp[inspermon.index(i)] + 25
                if exp[inspermon.index(i)]%100 == 0:
                    print(i)
                    insperdex_re[i][0] = insperdex_re[i][0]*(1.05)
                    insperdex_re[i][1] = insperdex_re[i][1]*(1.03)
                    insperdex[i][0] = insperdex_re[i][0]
                    insperdex[i][1] = insperdex_re[i][1]
                capturar(i,r,inspermon_am,ambiente_re,insperdex,insperdex_re,pedra)
                return
            if a == 0 and b == 0.2:
                print('Você perdeu {} de vida por dano de elemento'.format(so))
                print('Resultado:{}/{}'.format(vidajogador,vidaoponente))
                print('Você ganhou 25 xp')
                exp[inspermon.index(i)] = exp[inspermon.index(i)] + 25
                if exp[inspermon.index(i)]%100 == 0:
                   insperdex_re[i][0] = insperdex_re[i][0]*(1.05)
                   insperdex_re[i][1] = insperdex_re[i][1]*(1.03)
                   insperdex[i][0] = insperdex_re[i][0]
                   insperdex[i][1] = insperdex_re[i][1]
                capturar(i,r,inspermon_am,ambiente_re,insperdex,insperdex_re,pedra)
                return
        o = o + 1

#Função para capturar Inspermons (70% de chance de sucesso)
def capturar(i,r,inspermon_am,ambiente_re,insperdex,insperdex_re,pedra):
    c = random.randint(1,10)
    c = 1
    while True:
        capturar = input('Deseja capturar esse Inspermon ou pegar sua Pedra Preciosa?   (Digite a letra)\n(a)Capturar\n(b)Pegar Pedra Preciosa\n:')
        if capturar == 'a':
            if c <= 7:
                print(' ')
                print('Você conseguiu capturar o Inspermon')
                print(' ')
                insperdex[inspermon_am[r]] = ambiente_re[inspermon_am[r]][:]
                insperdex_re[inspermon_am[r]] = ambiente_re[inspermon_am[r]][:]
                return
            else:
                print(' ')
                print('Você não conseguiu capturar o Inspermon...')
                print(' ')
                return
        if capturar == 'b':
            print(' ')
            print('Você pegou a Pedra Preciosa')
            print(' ')
            pedra[0] = pedra[0] + 1
            return


jogo()

    
