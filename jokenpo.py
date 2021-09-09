def jogo_jokempo(): #função onde tem o código do jogo.

  print('Olá!')
  player1 = input("Digite o nome do Jogador 1: ")
  player2 = input('Agora digite o nome do Jogador 2: ')
  print()
  print('Ok', player1.title(),'e', player2.title(),'vamos jogar...')
  print()
  print(" *** PEDRA-PAPEL-TESOURA ***")
  print()
  print('JOGADOR 1')

  n1 = input('Coloque sua opção. pedra, papel ou tesoura: ')
  if n1 == 'pedra' or n1 == 'papel' or n1 == 'tesoura':
    print('Ok. gravei sua opção.')
  else:
    print('Digite uma opção válida.')
    while n1 != 'pedra' or n1 != 'papel' or n1 != 'tesoura':
      n1 = input('Coloque sua opção. pedra, papel ou tesoura: ')
      if n1 == 'pedra' or n1 == 'papel' or n1 == 'tesoura':
        print('Ok. Correto! ')
        break
      else:
        print('Digite novamente.')

  print("\x1b[2J")

  print('JOGADOR 2')
  n2 = input('Coloque sua opção. pedra, papel ou tesoura: ')
  if n2 == 'pedra' or n2 == 'papel' or n2 == 'tesoura':
    print('Ok. gravei sua opção.')
  else:
    print('Digite uma opção válida.')
    while not n2 == 'pedra' or not n2 == 'papel' or not n2 == 'tesoura':
      n2 = input('Coloque sua opção. pedra, papel ou tesoura: ')
      if n2 == 'pedra' or n2 == 'papel' or n2 == 'tesoura':
        print('Ok. gravei sua opção.')
        break
      else:
        print('Digite uma opção válida.')
  print("\x1b[2J")

  print('Agora vamos ao resultado...')
  print()

  if n1 == 'pedra' and n2 == 'papel':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print(player2.title(), 'VENCEU.')

  elif n1 == 'papel' and n2 == 'pedra':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print(player1.title(), 'VENCEU.')

  elif n1 == 'pedra' and n2 == 'tesoura':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print(player1.title(), 'VENCEU.')

  elif n1 == 'tesoura' and n2 == 'pedra':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print(player2.title(), 'VENCEU.')

  elif n1 == 'papel' and n2 == 'tesoura':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print(player2.title(), 'VENCEU.')

  elif n1 == 'tesoura' and n2 == 'papel':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print(player1.title(), 'VENCEU.')

  elif n1 == 'pedra' and n2 == 'pedra':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print('EMPATOU!!! NINGUÉM VENCEU. ')

  elif n1 == 'papel' and n2 == 'papel':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print('EMPATOU!!! NINGUÉM VENCEU. ')

  elif n1 == 'tesoura' and n2 == 'tesoura':
    print(player1.title(), 'colocou', n1.upper())
    print(player2.title(), 'colocou', n2.upper())
    print()
    print('EMPATOU!!! NINGUÉM VENCEU. ')

  print()
  print('   *** Jogo Finalizado! ***')
  print()

jogo_jokempo()
newgame = input('Para jogar novamente aperte qualquer tecla ou digite "sair" para fechar. ' )
if newgame == 'sair':
  print('Ok. Até mais.')
else:
  while newgame != 'sair':
    jogo_jokempo()
    newgame = input('Para jogar novamente aperte qualquer tecla ou digite "sair" para fechar. ')
  print("Ok. Até mais!")
