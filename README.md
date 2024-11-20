# Papel, Pedra ou Tesoura ✋✊✌️
Um jogo clássico, divertido e rápido de jogar diretamente no terminal! 🕹️

# 🎮 Sobre o Jogo
Este projeto é uma implementação simples e interativa do famoso jogo Papel, Pedra ou Tesoura, onde você pode desafiar o computador para ver quem é o melhor!

- **Como funciona?**
  - Escolha entre **Papel, Pedra** ou **Tesoura**.
  - O computador fará sua escolha aleatória.
  - As regras clássicas definem o vencedor:
    - Papel vence Pedra.
    - Pedra vence Tesoura.
    - Tesoura vence Papel.
  - O placar é atualizado automaticamente a cada rodada.

# 🛠️ Funcionalidades
  - **Sistema de Placar:** Mostra quantas rodadas você ganhou, perdeu ou empatou.
  - **Escolhas Aleatórias:** O computador escolhe de forma totalmente randômica.
  - **Interface Simples:** Interação direta com o usuário pelo terminal.
  - **Replay Ilimitado:** Jogue quantas vezes quiser!

# 📂 Estrutura do Código
  - ```gamelist:``` Define as opções do jogo (Papel, Pedra e Tesoura).
  - ```score:``` Mantém o placar atualizado.
  - **Funções principais:**
    - ```gameplay(i):``` Calcula o resultado de cada rodada (vitória, derrota ou empate).
    - ```gamescore(result, score):``` Atualiza o placar com base no resultado.

# 🚀 Como Jogar
  1. Certifique-se de ter o Python instalado na sua máquina (versão 3.x ou superior).
  2. Salve o código em um arquivo chamado papel_pedra_tesoura.py.
  3. Execute o programa no terminal:
    - ```
      ```
     python papel_pedra_tesoura.py
     
  4. Siga as instruções no terminal:
    - Escolha sua opção:
     - ```0:``` Papel
     - ```1:``` Pedra
     - ```2:``` Tesoura
   - Veja o resultado da rodada e o placar atualizado.
   - Escolha se deseja jogar novamente ou encerrar.

# 🔗 Exemplo de Execução
```
=========================================
Bem vindo ao jogo mais disputado do mundo

Papel Pedra ou Tesoura
=========================================

Placar:

Você: 1
Computador: 2
Empate: 0

Escolha sua opção: 

0 - Papel |  1 - Pedra |  2 - Tesoura
> 1

1...2...3...
Ahhh... Você Perdeu!!!

Sua escolha foi Pedra, a escolha do computador foi Papel. O resultado foi: Perdeu.

Deseja jogar novamente?
1 - Sim / 2 - Não
```
# 📖 Aprendizados e Técnicas Utilizadas
  - Bibliotecas do Python:
    - ```random:``` Para gerar escolhas aleatórias do computador.
    - ```os:``` Para limpar o terminal após cada rodada.
    - ```time:``` Para criar uma pausa dramática antes do resultado.
  - Manipulação de dicionários para organizar dados.
  - Estruturas de repetição e condicionais para controlar o fluxo do jogo.
#
Divirta-se jogando Papel, Pedra ou Tesoura! ✨  
Contribuições e sugestões são bem-vindas. 😊
