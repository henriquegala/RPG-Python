class Personagem:
    def __init__(self, nome, HP, attack, defense, speed):
        self.nome = nome #Nome do personagem
        self.HP = HP #0 até 100 (Baseado na altura)
        self.attack = attack #0 até 20 (Baseado no Gym)
        self.defense = defense #0 até 20 (Baseado no peso)
        self.speed = speed #0 até 10 (Baseado na resistência)

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
    print(f"{primeiro.nome} começa atacando primeiro!")
        
    turno = 1
        
    while primeiro.HP > 0 and segundo.HP > 0: #Loop para rodar os turnos de ataque
        print(f"Inicio do turno {turno}!")
        atacar(primeiro, segundo)
        
        if segundo.HP <= 0 or primeiro.HP <= 0:
            break
        
        atacar(segundo, primeiro)
        
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

def atacar(self, alvo):
    if self.HP > 0: #Ataque
        max_life = alvo.HP #Vida total antes do ataque
        alvo.HP = alvo.HP - ((self.attack/alvo.defense)*10) #Fórmula do ataque
        dano = max_life - alvo.HP #Dano dado após o ataque
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!\n {alvo.nome} está com {alvo.HP}")
    else:
        print(f"{self.nome} não pode atacar pois está sem vida!")

def character_selection():
    Henrique = Personagem("Galão", 60, 18, 18, 8)
    Rodrigo = Personagem("Rodrigão", 85,  14, 15, 14)
    Luis = Personagem("Luizão", 80, 10,  14, 18)
    Costa = Personagem("Costinha", 70, 16, 16, 16)
    Gil= Personagem("Gilzão", 90, 12, 16, 18)
    Tomas = Personagem("Tomzão", 85, 14, 16, 14)

    lista_lutadores = [Henrique, Rodrigo, Luis, Costa, Gil, Tomas]
    
    while True:
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

lutador1, lutador2 = character_selection()

iniciar_combate(lutador1,lutador2)

#FAZER:
# Sistema de quando as velocidades forem iguais fazer aleatoriamente quem começa
# Arredondar os valores da vida e do dano para 1 casa decimal
# Montar sistema de golpes (Cada um com 4 golpes que nem no Pokemon)
# ---Os golpes vão ser 1 de diminuir defesa(5 usos), 1 de diminuir ataque(5 usos), 1 de atacar(Infinitos usos), 1 de recuperar vida(3 usos)
# O sistema de golpes vai funcionar que nem no Pokemon, primeiro um usuário tem seu turno e seleciona o golpe que quer dar (alterando os status do alvo)
#e depois o segundo tem seu turno realizando a mesma coisa