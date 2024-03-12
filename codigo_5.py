'''
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente 
definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
'''

def reverte_string(frase: str) -> str:
    return frase[::-1]

while True:
    frase = input('Frase que deseja revertar [digite "sair" para fechar]: ')
    if frase == 'sair':
        break
    print(reverte_string(frase=frase))