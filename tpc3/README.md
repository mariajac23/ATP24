# TPC 3 

Função MostrarMenu()
Esta função exibe um menu principal com três opções:

Modo Normal (o jogador joga primeiro e o computador sempre vence)
Modo Computador (o computador joga primeiro)
Sair do jogo
Função sair()
Esta função mostra uma mensagem de despedida quando o jogador escolhe sair do jogo pelo menu.

Função modonormal()
Esta função implementa o modo normal do jogo, onde o jogador começa e o computador garante sua vitória seguindo uma estratégia específica.

Passos:

Inicia o jogo com 21 fósforos.
Turno do jogador:
O jogador escolhe quantos fósforos remover (1, 2, 3 ou 4). O código assegura que a entrada seja válida, pedindo ao jogador para tentar novamente em caso de valor inválido.
Após uma jogada válida, o número de fósforos restantes é atualizado.
Verifica se o número de fósforos chegou a zero. Se sim, o jogador perde.
Turno do computador:
Se houver fósforos restantes, o computador faz sua jogada. Ele garante a vitória ao remover fósforos de forma que a soma dos fósforos removidos pelo jogador e pelo computador seja 5, sempre que possível, forçando o jogador a ficar com o último fósforo.
Se restarem menos de 5 fósforos, o computador remove todos exceto o último.
Após a jogada do computador, o número de fósforos restantes é atualizado e verifica se o jogo acabou.
Essa estratégia garante que o computador sempre vença, desde que o jogador comece primeiro.

Função modocomputador()
Esta função implementa o modo em que o computador começa jogando. A principal diferença é que, neste modo, o computador faz a primeira jogada.

Passos:

Inicia o jogo com 21 fósforos.
Turno do computador:
O computador escolhe aleatoriamente quantos fósforos remover (entre 1 e 4), utilizando a função random.randint().
O número de fósforos restantes é atualizado, e verifica se o computador venceu removendo o último fósforo.
Turno do jogador:
O jogador escolhe quantos fósforos remover (1, 2, 3 ou 4), com a mesma validação do modo normal.
O número de fósforos restantes é atualizado, verificando se o jogador retirou o último fósforo e perdeu.
Neste modo, o computador não segue uma estratégia específica, permitindo que o jogador vença dependendo de suas jogadas.

Função menu()
Esta função controla o fluxo do jogo, permitindo ao jogador escolher entre as opções:

Jogar o modo normal
Jogar o modo em que o computador começa
Sair do jogo
Passos:

Exibe o menu principal por meio da função MostrarMenu().
Solicita ao jogador que escolha uma opção (1, 2 ou 0) e, com base na escolha:
Chama a função modonormal() se a escolha for 1.
Chama a função modocomputador() se a escolha for 2.
Chama a função sair() se a escolha for 0.
Valida a entrada do usuário para evitar valores inválidos, mostrando uma mensagem de erro em caso de erro.
