import random
import os
import time

os.system('cls')
print("=========================================")
print("Bem vindo ao jogo mais disputado do mundo")
print("")
print("Papel Pedra ou Tesoura")
print("=========================================")

gamelist = {0:'Papel',
            1:'Pedra',
            2:'Tesoura'}

score = {'you':0,
        'pc':0,
        'draw':0}

result = {1:'Perdeu',
          2:'Ganhou',
          3:'Empate'}

def gameplay(i):
    pc_select = random.randrange(0,3)
    #result: 1 = loss, 2 = win , 3 = draw
    if i == pc_select:
        result=3
        return i,pc_select,result 
    elif i ==0 and pc_select ==1:
        result=2
        return i,pc_select,result
    elif i ==0 and pc_select ==2:
        result=1
        return i,pc_select,result
    elif i ==1 and pc_select ==0:
        result=1
        return i,pc_select,result
    elif i ==1 and pc_select ==2:
        result=2
        return i,pc_select,result
    elif i ==2 and pc_select ==1:
        result=1
        return i,pc_select,result
    elif i ==2 and pc_select ==0:
        result=2
        return i,pc_select,result
    

def gamescore(result,score):
    
    if result == 3:
        score['draw'] = score['draw']+1
    elif result == 2:
        score['you'] = score['you']+1
    else:
        score['pc'] = score['pc']+1
    return score

while True:
    print("")
    print("Placar:\n")
    print("Você:{}".format(score['you']))
    print("Computador:{}".format(score['pc']))
    print("Empate:{}".format(score['draw']))
    print("")
    print("Escolha sua opção: \n")
    print("0 - Papel |  1 - Pedra |  2 - Tesoura")

    your_input =int(input())
    
    result_game = gameplay(your_input)
    
    gamescore(result_game[2],score)

    print('1...2...3...')
    time.sleep(2)
    os.system('cls')
    if result_game[2] == 1:
        print("Ahhh...Voce Perdeu!!!\n")
        print('Sua escolha foi {}, a escolha do computador foi {}. o resultado foi: {}'.format(gamelist[result_game[0]],gamelist[result_game[1]],result[result_game[2]]))
    elif result_game[2] == 2:
        print("Uhuuuu...Voce Ganhou!!!\n")
        print('Sua escolha foi {}, a escolha do computador foi {}. o resultado foi: {}'.format(gamelist[result_game[0]],gamelist[result_game[1]],result[result_game[2]]))
    elif result_game[2] == 3:
        print("Eitaa...Empatou!!!\n")
        print('Sua escolha foi {}, a escolha do computador foi {}. o resultado foi: {}'.format(gamelist[result_game[0]],gamelist[result_game[1]],result[result_game[2]]))
    print("")
    print("Deseja jogar novamente?\n")
    print("1 - Sim / 2 - Não")   
    

    game_again = int(input())

    if game_again == 2:
        exit()
    else:
        os.system('cls')
