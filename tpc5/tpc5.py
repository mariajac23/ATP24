#Tpc5- python

import random

sala1 = [60, [], "Shrek 1"]
sala2 = [80, [], "Shrek 2"]
sala3 = [30, [], "Shrek 3"]
sala4 = [75, [], "Shrek 4"]

cinema = [sala1, sala2, sala3, sala4]

def MostrarMenu():
    print(''' Bem-vindo à aplicação cinema!
              O que deseja fazer?
          
              -----------MENU--------------
              (1) Filmes em exibição-------
              (2) Comprar bilhete----------
              (3) Disponibiliade de sala---
              (4) Inserir Sala-------------
              (0) Sair---------------------''')
  
    
def existesala(cinema, sala): #lista de salas e sala
    cond = False
    for s in cinema:
      if s [2] == sala[2]:#  verifica se a sala existe (neste caso 2 -> é o filme,  uma sala tem um único filme)
        cond = True
      return cond
    
def inserirsala(cinema, sala):
    if not existesala(cinema, sala):
      cinema.append(sala)
    return cinema
    
def listar(cinema): 
    if cinema:
      print("----Lista de filmes em exibição!----")
      for s in cinema:
        print(f"Filme em exibição: {s[2]} | Lotação máxima da sala: {s[0]}")
    
    else:
       print("Nenhum filme em exibição no momento.")
    return
        
def disponivel(cinema, filmecin, lugar): #verificar de sala não está com lotação máxima
    cond = True
    for sala in cinema:
      nlugares, vendidos, filme = sala
      if filmecin == filme and lugar <= nlugares:
        if lugar in vendidos:
           cond = False
    return cond
        
def venderBilh(cinema, filmecin, lugar):      
  for sala in cinema:
      nlugares, vendidos, filme = sala  
      if filme == filmecin:
          if disponivel(cinema, filmecin, lugar):
              vendidos.append(lugar)
              print(f"Lugar {lugar} comprado na sala do filme {filmecin}.")
          else:
              print("O lugar {lugar} está indisponível para a sala do filme {filmecin}")
          return cinema
    
def listardisponibilidades(cinema):
    for sala in cinema:
        nlugares, vendidos, filme = sala
        disponiveis = nlugares - len(vendidos)
        print(f"O sala que exibe o filme {filme} tem {disponiveis} lugares disponíveis")

def cria_sala(cinema, filmecin, lugares):
    nova_sala = [int(lugares), [], filmecin]
    return inserirsala(cinema, nova_sala)
    
def sair():
    print("Saiu da aplicação. Até breve!")

def Menu():
  global cinema

  while True:
    MostrarMenu()
    opcao = int(input("Qual a opção que quer abrir?"))

    if opcao == 0:
      sair()
      break

    elif opcao == 1:
      listar(cinema)

    elif opcao == 2:
      filmecin = input("Qual o fime que deseja ver?")
      lugar = int(input("Número de lugar: ")) 
      cinema = venderBilh(cinema, filmecin, lugar)

    elif opcao == 3:
      listardisponibilidades(cinema)

    elif opcao == 4:
      filmecin = input("Qual filme deseja adicionar ao cinema?")
      lugares = input("Quantos lugares terá essa nova sala?")
      cinema = cria_sala(cinema, filmecin, lugares)

    else:
       print("Opção inválida. Tente novamente")
        
          
Menu()