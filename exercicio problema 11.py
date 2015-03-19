from random import randint
scorep2 = 0
scorep1 = 0
while (scorep1 < 3 and scorep2 < 3):
    number = randint(1,5)
    choose_char = input('Escolha um Pedra/papel/tesoura/lagarto ou spock:\n')
    if number == 1 and choose_char == 'lagarto':
        scorep1 = scorep1 + 1
        print('')
    if number == 1 and choose_char == 'papel':
        scorep1 = scorep1 + 1 
    if number == 2 and choose_char == 'pedra':
        scorep1 = scorep1 + 1 
    if number == 2 and choose_char == 'spock':
        scorep1 = scorep1 + 1 
    if number == 3 and choose_char == 'tesoura':
        scorep1 = scorep1 + 1 
    if number == 3 and choose_char == 'lagarto':
        scorep1 = scorep1 + 1 
    if number == 4 and choose_char == 'papel':
        scorep1 = scorep1 + 1 
    if number == 4 and choose_char == 'spock':
        scorep1 = scorep1 + 1 
    if number == 5 and choose_char == 'pedra':
        scorep1 = scorep1 + 1 
    if number == 5 and choose_char == 'tesoura':
        scorep1 = scorep1 + 1 
    if number == 1 and choose_char == 'pedra':
        scorep2 = scorep2 + 1
    if number == 1 and choose_char == 'tesoura':
        scorep2 = scorep2 + 1 
    if number == 2 and choose_char == 'lagarto':
        scorep2 = scorep2 + 1 
    if number == 2 and choose_char == 'papel':
        scorep2 = scorep2 + 1 
    if number == 3 and choose_char == 'pedra':
        scorep2 = scorep2 + 1 
    if number == 3 and choose_char == 'spock':
        scorep2 = scorep2 + 1 
    if number == 4 and choose_char == 'tesoura':
        scorep2 = scorep2 + 1 
    if number == 4 and choose_char == 'lagarto':
        scorep2 = scorep2 + 1 
    if number == 5 and choose_char == 'spock':
        scorep2 = scorep2 + 1 
    if number == 5 and choose_char == 'papel':
        scorep2 = scorep2 + 1     
    if number == 1 and choose_char == 'spock':
        print('empate')
    if number == 2 and choose_char == 'tesoura':
        print('empate') 
    if number == 3 and choose_char == 'papel':
        print('empate') 
    if number == 4 and choose_char == 'pedra':
        print('empate') 
    if number == 5 and choose_char == 'lagarto':
        print('empate')     
    print('pontuação p1:%d'%scorep1,'\npontuação computador:%d'%scorep2)
if scorep1 == 3:
    print('Parabéns você é o campeão')
if scorep2 == 3:
    print('Você perdeu!!')
        