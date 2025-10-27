import random

class Personagem:
    def __init__(self, nome, HP, attack, defense, speed, golpes): #Define a classe de personagem 
        self.nome = nome #Nome do personagem
        self.HP = HP #0 até 100 (Baseado na altura)
        self.attack = attack #0 até 20 (Baseado no Gym)
        self.defense = defense #0 até 20 (Baseado no peso)
        self.speed = speed #0 até 10 (Baseado na resistência)
        self.golpes = golpes
    
    def usar_golpe(self, alvo, golpe): #Define a função usar golpe
        print(f"{self.nome} usou {golpe.nome_golpe}")
        
        if self.HP <= 0: #Verifica a vida do atacante
            print(f"{self.nome} está sem vida e não pode agir!")
            return
        
        if golpe.uso_atual <= 0: #Verifica o PP do golpe a ser usado
            print(f"{golpe.nome_golpe} não tem mais usos (PP)!")
        
        golpe.uso_atual -= 1
        
        tipo = golpe.tipo_efeito
        dano_base_golpe = golpe.dano_base #AINDA ESTÁ INCOMPLETO
        valor_efeito = golpe.valor_efeito
        
        if tipo == "DANO": #Define o tipo de golpe que é
            if self.HP > 0: #Ataque
                max_life = alvo.HP #Vida total antes do ataque
                alvo.HP = round(alvo.HP - ((self.attack/alvo.defense)*10)) #Fórmula do ataque
                dano = (max_life - alvo.HP) #Dano dado após o ataque
                print(f"💥 {self.nome} atacou {alvo.nome} causando {dano} de dano!\n {alvo.nome} está com {alvo.HP} HP!")
            else:
                print(f"{self.nome} não pode atacar pois está sem vida!")
        
        elif tipo == "CURA": #Define o tipo de golpe que é
            self.HP += valor_efeito
            print(f"💚 {self.nome} recuperou {valor_efeito} de HP!")
        
        elif tipo == "BUFF DEFESA": #Define o tipo de golpe que é
            self.defense += valor_efeito
            print(f"⬆️ Defesa do {self.nome} aumentada para {self.defense}")
        
        elif tipo == "BUFF DANO": #Define o tipo de golpe que é
            self.attack += valor_efeito
            print(f"⬆️ Ataque de {self.nome} aumentada para {self.attack}")
        
        else:
            print("Este golpe tem um efeito desconhecido!")
        
        print(f"Usos restantes {golpe.nome_golpe}: {golpe.uso_atual}")

class Golpe: #Classe para definir os golpes
    def __init__(self, nome_golpe, dano_base, uso_maximo, tipo_efeito, valor_efeito):
        self.nome_golpe = nome_golpe #Nome do golpe
        self.dano_base = dano_base #Dano base do golpe
        self.uso_maximo = uso_maximo #Uso máximo deste golpe
        self.uso_atual = uso_maximo #Quantos usos já tiveste deste golpe
        self.tipo_efeito = tipo_efeito #Tipo do golpe
        self.valor_efeito = valor_efeito #Valor que o golpe altera

def selecao_execucao_golpe(atacante, alvo): #Define como funciona a execução dos golpes
    if atacante.HP <= 0: #Verifica a vida do atacante
        return
    
    while True: #Loop para fazer a escolha do golpe
        print(f"Vez de {atacante.nome}!")
        print("Escolha um golpe:")
        
        for i, g in enumerate(atacante.golpes): #Ve a lista de golpes que o atacante têm
            numero_escolha = i + 1
            print(f"({numero_escolha}) {g.nome_golpe} (PP: {g.uso_atual}/{g.uso_maximo})")
            
        escolha = int(input("Introduza o número do golpe:"))
        
        if not (1 <= escolha <= len(atacante.golpes)):
            print("Número de golpe inválido. Tente novamente.")
            continue
        
        golpe_escolhido = atacante.golpes[escolha - 1]
        
        atacante.usar_golpe(alvo, golpe_escolhido)
        break

def iniciar_combate(player1, player2): #Decide quem começa a luta
    print("INICIAR COMBATE")
    print(f"{player1.nome} (Vel: {player1.speed}) vs {player2.nome} (Vel: {player2.speed})")
        
    if player1.speed > player2.speed: #Decide que começa a luta pela velocidade
        primeiro = player1
        segundo = player2
    elif player1.speed < player2.speed:
        primeiro = player2
        segundo = player1
    else:
        combatentes = [player1, player2]
        primeiro = random.choice(combatentes)
        if primeiro == player1:
            segundo = player2
        else:
            segundo = player1
    print(f"{primeiro.nome} começa atacando primeiro!")
        
    turno = 1
        
    while primeiro.HP > 0 and segundo.HP > 0: #Loop para rodar os turnos de ataque
        print(f"Inicio do turno {turno}!")
        
        selecao_execucao_golpe(primeiro, segundo)
        
        if segundo.HP <= 0 or primeiro.HP <= 0:
            break
        
        selecao_execucao_golpe(segundo, primeiro)
        
        if segundo.HP <= 0 or primeiro.HP <= 0:
            break
        
        turno += 1
    print("\n FIM DO COMBATE")
    
    if primeiro.HP > 0 and segundo.HP <= 0:
        print(f"Vitória para {primeiro.nome}!")
    elif primeiro.HP <= 0 and segundo.HP > 0:
        print(f"Vitória para  {segundo.nome}")
    elif primeiro.HP == 0 and segundo.HP == 0:
        print("Empate!")
    else:
        print("Resultado inesperado!")

def character_selection(): #Defino os personagens da batalha
    Henrique_temp = Personagem("Galão", 60, 18, 18, 8, []) 
    Rodrigo_temp = Personagem("Rodrigão", 85, 14, 15, 14, [])
    Luis_temp = Personagem("Luizão", 80, 10, 14, 18, [])
    Costa_temp = Personagem("Costinha", 70, 16, 16, 16, [])
    Gil_temp = Personagem("Gilzão", 90, 12, 16, 18, [])
    Tomas_temp = Personagem("Tomzão", 85, 14, 16, 14, [])
    
    lista_golpes_Henrique = golpes_Henrique(Henrique_temp.attack)
    lista_golpes_Rodrigo = golpes_Rodrigo(Rodrigo_temp.attack)
    lista_golpes_Luis = golpes_Luis(Luis_temp.attack)
    lista_golpes_Costa = golpes_Costa(Costa_temp.attack)
    lista_golpes_Gil = golpes_Gil(Gil_temp.attack)
    lista_golpes_Tomas = golpes_Tomas(Tomas_temp.attack)
    
    Henrique = Personagem("Galão", 60, 18, 18, 8, lista_golpes_Henrique)
    Rodrigo = Personagem("Rodrigão", 85,  14, 15, 14, lista_golpes_Rodrigo)
    Luis = Personagem("Luizão", 80, 10,  14, 18, lista_golpes_Luis)
    Costa = Personagem("Costinha", 70, 16, 16, 16, lista_golpes_Costa)
    Gil= Personagem("Gilzão", 90, 12, 16, 18, lista_golpes_Gil)
    Tomas = Personagem("Tomzão", 85, 14, 16, 14, lista_golpes_Tomas)

    lista_lutadores = [Henrique, Rodrigo, Luis, Costa, Gil, Tomas]
    
    while True: #Loop para fazer a escolha dos personagens
        escolha_1 = int(input("CHOOSE YOUR FIGHTER: (1)-Galão; (2)-Rodrigão; (3)-Luizão; (4)-Costinha; (5)-Gilzão; (6)-Tomzão:\n"))

        if escolha_1 < 1 or escolha_1 > 6:
            print("Introduza um lutador válido!")
            continue
        else:
            c1_obj = lista_lutadores[escolha_1 - 1]
        
        escolha_2 = int(input("CHOOSE YOUR FIGHTER: (1)-Galão; (2)-Rodrigão; (3)-Luizão; (4)-Costinha; (5)-Gilzão; (6)-Tomzão:\n"))
        
        if escolha_2 < 1 or escolha_2 > 6:
            print("Introduza um lutador válido!")
            continue
        else:
            c2_obj = lista_lutadores[escolha_2 - 1]
        
        if escolha_1 == escolha_2:
            print("Não podes lutar contra si mesmo!")
            continue
        
        return c1_obj, c2_obj

def golpes_Henrique(ataque_base): #Define o golpe dos lutadores
    golpe_1 = Golpe("Socada forte", dano_base=18, uso_maximo=100, tipo_efeito="DANO", valor_efeito=0)
    golpe_2 = Golpe("Aplicada", dano_base=0, uso_maximo=3, tipo_efeito="BUFF DANO", valor_efeito=3)
    golpe_Henrique = [golpe_1, golpe_2]
    return golpe_Henrique

def golpes_Rodrigo(ataque_base): #Define o golpe dos lutadores
    golpe_1 = Golpe("Xinada por trás", dano_base=14, uso_maximo=100, tipo_efeito="DANO", valor_efeito=0)
    golpe_2 = Golpe("Chillada", dano_base=0, uso_maximo=3, tipo_efeito="BUFF DEFESA", valor_efeito=3)
    golpe_Rodrigo = [golpe_1, golpe_2]
    return golpe_Rodrigo

def golpes_Luis(ataque_base): #Define o golpe dos lutadores
    golpe_1 = Golpe("Chapada", dano_base=10, uso_maximo=100, tipo_efeito="DANO", valor_efeito=0)
    golpe_2 = Golpe("Rage bait", dano_base=0, uso_maximo=3, tipo_efeito="DEBUFF DANO", valor_efeito=3)
    golpe_Luis = [golpe_1, golpe_2]
    return golpe_Luis

def golpes_Costa(ataque_base): #Define o golpe dos lutadores
    golpe_1 = Golpe("One tap", dano_base=16, uso_maximo=100, tipo_efeito="DANO", valor_efeito=0)
    golpe_2 = Golpe("Petinga", dano_base=0, uso_maximo=3, tipo_efeito="CURA", valor_efeito=5)
    golpe_Costa = [golpe_1, golpe_2]
    return golpe_Costa

def golpes_Gil(ataque_base): #Define o golpe dos lutadores
    golpe_1 = Golpe("Entrada criminosa", dano_base=12, uso_maximo=100, tipo_efeito="DANO", valor_efeito=0)
    golpe_2 = Golpe("Gelinho", dano_base=0, uso_maximo=3, tipo_efeito="BUFF DEFESA", valor_efeito=2)
    golpe_Gil = [golpe_1, golpe_2]
    return golpe_Gil

def golpes_Tomas(ataque_base): #Define o golpe dos lutadores
    golpe_1 = Golpe("Ultada potente", dano_base=14, uso_maximo=100, tipo_efeito="DANO", valor_efeito=0)
    golpe_2 = Golpe("Ultra flex", dano_base=0, uso_maximo=3, tipo_efeito="DEBUFF DEFESA", valor_efeito=2)
    golpe_Tomas = [golpe_1, golpe_2]
    return golpe_Tomas

lutador1, lutador2 = character_selection() #Inicia a seleção dos personagens

iniciar_combate(lutador1,lutador2) #Inicia o combate com os personagens selecionados

#FAZER:
# Incrementar golpes de BUFF/DEBUFF
# Incrementar a questão do ataque base, vida max...... para ajustar para com os BUFFS e DEBUFFS