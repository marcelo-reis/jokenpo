from random import randint
from emoji import emojize

invert = '\033[1;7m'
amarelo = '\033[33m'
limpa = '\033[m'
ppt = {1:'Pedra', 2:'Papel', 3:'Tesoura'}
pptmj = {1:':punch:', 2:':raised_hand:', 3:':v:'}

print(
    '''      _    ___            _  __  _____   _   _           ____     ___  
     | |  / _ \          | |/ / | ____| | \ | |         |  _ \   / _ \ 
  _  | | | | | |  _____  | ' /  |  _|   |  \| |  _____  | |_) | | | | |
 | |_| | | |_| | |_____| | . \  | |___  | |\  | |_____| |  __/  | |_| |
  \___/   \___/          |_|\_\ |_____| |_| \_|         |_|      \___/ 
''')
mychoice = int(input('Pedra  {}(1){}\n'
                'Papel  {}(2){}\n'
                'Tesoura{}(3){}\n'
                'Escolha a opção: ' .format(invert,limpa, invert, limpa, invert, limpa)))
pcchoice = randint(1, 3)
print('-'*20)
print(emojize('Você escolheu {}{}{} {}{}{} e eu {}{}{} {}{}{}:'
      .format(invert,ppt[mychoice],limpa,amarelo,pptmj[mychoice],limpa,amarelo,pptmj[pcchoice],limpa,invert,ppt[pcchoice],limpa), use_aliases=True))
print('e...')

# Pedra
if ppt[mychoice] == 'Pedra' and ppt[pcchoice] == 'Pedra':
    print('Empate! {}{}{} e {}{}{}' .format(invert, ppt[mychoice],limpa,invert,ppt[pcchoice],limpa))
elif ppt[mychoice] == 'Pedra' and ppt[pcchoice] == 'Papel':
    print('Perdeu! {}{}{} vence {}{}{}'.format(invert, ppt[pcchoice], limpa, invert, ppt[mychoice], limpa))
elif ppt[mychoice] == 'Pedra' and ppt[pcchoice] == 'Tesoura':
    print('Venceu! {}{}{} vence {}{}{}'.format(invert, ppt[mychoice], limpa, invert, ppt[pcchoice], limpa))
# Papel
elif ppt[mychoice] == 'Papel' and ppt[pcchoice] == 'Pedra':
    print('Venceu! {}{}{} vence {}{}{}'.format(invert, ppt[mychoice], limpa, invert, ppt[pcchoice], limpa))
elif ppt[mychoice] == 'Papel' and ppt[pcchoice] == 'Papel':
    print('Empate! {}{}{} e {}{}{}' .format(invert, ppt[mychoice],limpa,invert,ppt[pcchoice],limpa))
elif ppt[mychoice] == 'Papel' and ppt[pcchoice] == 'Tesoura':
    print('Perdeu! {}{}{} vence {}{}{}'.format(invert, ppt[pcchoice], limpa, invert, ppt[mychoice], limpa))
# Tesoura
elif ppt[mychoice] == 'Tesoura' and ppt[pcchoice] == 'Pedra':
    print('Perdeu! {}{}{} vence {}{}{}'.format(invert, ppt[pcchoice], limpa, invert, ppt[mychoice], limpa))
elif ppt[mychoice] == 'Tesoura' and ppt[pcchoice] == 'Papel':
    print('Venceu! {}{}{} vence {}{}{}'.format(invert, ppt[mychoice], limpa, invert, ppt[pcchoice], limpa))
else:
    print('Empate! {}{}{} e {}{}{}' .format(invert, ppt[mychoice],limpa,invert,ppt[pcchoice],limpa))





