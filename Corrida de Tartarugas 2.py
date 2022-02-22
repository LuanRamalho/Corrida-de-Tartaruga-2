# Importando módulos
import turtle
import random

# Criando Tartaruga
tartaruga = turtle.Turtle()
# Para desenhar mais rápido
tartaruga.speed(0)
# Posição inicial para a criação das linhas tupla(x, y)
posicao_inicial = (-300, 200)
# Espaçamento
espacamento = 30
# Desativando a caneta antes de qualquer movimento
tartaruga.penup()
# Movendo a tartaruga para a posição inicial e apontando para baixo
tartaruga.right(90)
tartaruga.setpos(posicao_inicial[0], posicao_inicial[1])
# Faça 20 vezes, para criar 20 linhas
for step in range(0, 20):
    # Escrevendo número da linha
    tartaruga.write(step + 1)  # step+1 pois começa em 0
    # Ativando a caneta
    tartaruga.pendown()
    # Criando linha pontilhada de tamanho 400
    for step in range(0, 40):
        # Ativando e desativando a caneta
        if step % 2 == 0:
            tartaruga.penup()
        else:
            tartaruga.pendown()
        # Anda 10 pixels pra frente
        tartaruga.forward(10)
    # Desativando a caneta
    tartaruga.penup()
    # Indo para a próxima posição
    novo_x = tartaruga.pos()[0] + espacamento
    novo_y = posicao_inicial[1]
    tartaruga.setpos(novo_x, novo_y)
# Dados das tartarugas
nomes = ["Vermelho", "Azul", "Amarelo", "Verde", "Roxo"]
cores = ["red", "blue", "yellow", "green", "purple"]
# Dicionário que armazenará as tartarugas
tartarugas = dict()
# Posição de largada
posicao_largada = (-330, 150)
espacamento = 50
# Criando cada Tartaruga
for nome, cor in zip(nomes, cores):
    tartarugas[nome] = turtle.Turtle()
    tartarugas[nome].shape("turtle")
    tartarugas[nome].color(cor)
    # Movendo para a posição de larga
    pos_x = posicao_largada[0]
    pos_y = posicao_largada[1] - (espacamento * len(tartarugas))
    tartarugas[nome].penup()
    tartarugas[nome].setpos(pos_x, pos_y)
    # Passos para dar uma volta completa
    passos = 8
    for passo in range(0, passos):
        tartarugas[nome].right(360 / passos)

    tartarugas[nome].pendown()
# Variável pra armazenar o nome da tartaruga vencedora
vencedora = ""
# Enquanto não houver vencedora
while not vencedora:
    # Nomes é uma lista com todos os nomes das tartarugas
    for nome in nomes:
        # Obtendo a distância
        distancia = random.randint(1, 5)
        # Fazendo a tartaruga andar a distância
        tartarugas[nome].forward(distancia)

        # Verificando se essa tartaruga venceu
        if tartarugas[nome].pos()[0] > 300:
            vencedora = nome
            break
# "tartaruga" é a nossa tartaruga que desenhou a pista de corrida
tartaruga.penup()
tartaruga.setposition(0, -300)
mensagem = "A tartaruga vencedora foi: {}".format(vencedora)
# Fonte com Nome, tamanho e forma
fonte = ("Comic Sans", 20, "bold")
# Texto, move a tartaruga para o final, alinhamento e e fonte
tartaruga.write(mensagem, True, "center", fonte)
# Movendo a tartaruga vencedora
tartarugas[vencedora].penup()
tartarugas[vencedora].setposition(0, -330)
# Comemorando
while True:
    tartarugas[vencedora].right(10)