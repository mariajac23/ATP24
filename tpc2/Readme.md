# TPC 2 - Adivinha o numero 

Este exercício propõe criar um jogo em Python chamado "Adivinhar o Número", que tem dois modos:

Modo Computador: O computador gera um número aleatório de 0 a 100, e o jogador deve adivinhar. O jogo dá dicas (maior/menor) até que o número seja o certo.

Modo Normal: O jogador pensa num número de 0 a 100, e o computador tenta adivinhar usando um algoritmo de busca binária, ajustando o intervalo de possibilidades de acordo com as respostas do jogador.

O jogo começa apresentando um menu com as duas opções (computador e normal) e uma opção para sair. Cada modo possui um contador que regista as tentativas até que o número seja adivinhado.

- **Opção 1:** Modo Computador – o jogador tenta adivinhar o número.
- **Opção 2:** Modo Normal – o computador adivinha o número do jogador.
- **Opção 0:** Sair – para encerrar o jogo.

# Opção 1: 
O número aleatório é criado pela função random.randint(0, 100) e armazenado na variável num.

Um contador de tentativas, i, inicia em 0 e é incrementado a cada tentativa do jogador.
O jogador fornece o seu palpite através do comando input, que é convertido num valor inteiro.
Para cada palpite, o programa verifica se o número do jogador é:
-Igual ao número: Caso o jogador acerte, o programa exibe uma mensagem de parabéns com o número de tentativas e finaliza o jogo.
-Maior que o número: Caso o palpite seja maior, o jogo informa que o número gerado pelo computador é menor.
-Menor que o número: Caso o palpite seja menor, o jogo informa que o número gerado é maior.

# Opção 2: 
Aqui, o jogador pensa em um número entre 0 e 100, e o computador tenta adivinhar esse número. Este modo usa um algoritmo de busca binária, que permite ao computador fazer palpites eficientes ajustando o intervalo de possibilidades.

- O jogador pensa em um número, e o intervalo de possibilidades inicialmente é de 0 a 100, representado pelas variáveis `menor` e `maior`.
- O palpite do computador é calculado como a média do intervalo atual: `(maior + menor) // 2`. Este valor, `tenta`, é o que o computador acredita ser o número.
- O jogador deve responder com "Acertou", "Maior" ou "Menor" para orientar o computador:
  - Se o jogador disser **"Acertou"**, o jogo termina e o computador exibe o número de tentativas que levou para adivinhar.
  - Se o jogador disser **"Maior"**, significa que o número que o computador pensou é menor do que o real, então o limite inferior do intervalo (`menor`) é atualizado para `tenta + 1`.
  - Se o jogador disser **"Menor"**, significa que o número que o computador pensou é maior do que o real, então o limite superior do intervalo (`maior`) é atualizado para `tenta - 1`.
- O jogo continua até que o computador acerte o número.