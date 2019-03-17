'''
dia = input ('nasceste em que dia ?')
mes = input ('nasceste em que mes ?')
ano = input ('nasceste em que ano ?')
print ('este pino nasces no dia', dia,',no mes', mes,',no ano', ano,', porque e granda pino')
'''
'''
numero1 = input('dame um numero.')
numero2 = input('dame outro numero, porfavor')
print (int(numero1) + int(numero2))
'''
'''
n1 = int(input('digite um numero'))
n2 = int(input('digite outro numero'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
p = n1**n2
print('a soma dos dois numeros e {},a multiplicacao e {} e a divisao {}'.format(s, m, d))
print('a divisao inteira e {} e a potencia e {}'.format(di, m))
'''
'''
n1 = int(input('digite um numero'))
n2 = n1+1
n3 = n1-1
print('o sucessor do numeero e {} e o antecessor e {}'.format(n2 ,n3))
'''
'''
n1 = int(input('digite um numero'))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1 ** (1/2)
print('o dobro do numero e {}, o triplo e {}, e a raiz quadrada e {}'.format(n2, n3, n4))
'''
'''
nota1 = int(input('qual foi a tua nota a cps ?'))
nota2 = int(input('qual foi a tua nota a pcm ?'))
media = (nota1 + nota2) / 2
print('a media do ze a cps e pcm foi ', media)
'''
'''
metros = int(input('quantos metros percorres ate ao trabalho ?'))
cent = metros * 100
mili = metros * 1000
print('o ze percorre {} centimetros e {} milimetros de casa ao skatepark'.format(cent ,mili))
'''
'''
n1 = int(input('escolhe um numero'))
for e in range(1,11):
    print(n1*e)
'''
'''
l = int(input('lurgura:'))
a = int(input('altura:'))
area = l * a
litro = area / 2
print('a area da parede e {} e a quantidade de tinta é {}'.format(area, litro))
'''
'''
preco = int(input('o preco do carro é'))
desc = preco * 0.05
pf = preco - desc
print('o preco é {} mas com desconto de 5% fica a {}'.format(preco, pf))
'''
'''
si = int(input('qual o seu salario hoje em dia na companhia ?'))
aumento = si * 0.15
ns = si + aumento
print('o seu novo salario vai ser', ns)
'''
'''
import math
n1 = int(input('digite um numero'))
raiz = math.sqrt(n1)
print('a raiz quadrada de {} vai ser {:.2f}'.format(n1, raiz))
'''
'''
import math
n1 = float(input('digite um numero'))
n2 = math.floor(n1)
print('a porcao real do numero e:', n2)
'''
'''
import math
c1 = int(input('digite o cateto'))
c2 = int(input('digite o outro cateto'))
c12 = c1**2 + c2**2
h = math.sqrt(c12)
print('o comprimento da hipotnusa e:', h)
'''
'''
import math
a = int(input('digite um angulo'))
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print('o seno deste angulo e {} o coseno deste angulo e {} e por fim a tangente deste angulo e {}'.format(s, c, t))
'''
'''
from random import choices
a1 = input('primeiro aluno')
a2 = input('segundo aluno')
a3 = input('terceiro aluno')
a4 = input('quarto aluno')
lista = [a1, a2, a3, a4]
escolhido = choices (lista)
print('o aluno escolhido foi {}'.format(escolhido))
'''
'''
from random import shuffle
a1 = input('aluno 1')
a2 = input('aluno 2')
a3 = input('aluno 3')
a4 = input('aluno 4')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('a ordem de apresentacao dos trabalhos e a seguinte:{}'.format(lista))
'''
'''
lista = [[1, 2],[3, 4]]
for x in range (len(lista)):
    print(lista[x])
'''
'''
lista = [13, 15, 1, 0, 2, 8, 9, 10]
def lis(lista):
    for x in range (len(lista)):
        if lista[x]%2 == 0:
             lista[x] = lista[x] *2
    return lista
print(lis(lista))
'''
'''
frase = 'curso em video python'
frase = frase.replace('python', 'andriod')
print(frase)
'''
'''
nome = input('qual o teu nome completo ?').strip()
nomeu = (nome.upper())
nomel = (nome.lower())
qnome = (len(nome) - (nome.count(' ')))
pnome = (nome.find(' '))
print('o teu nome e ', nome)
print(' o teu nome completo em maiusculas e ', nomeu)
print('o teu nome completo em minusculas  e ', nomel)
print('o nome tem ao todo', qnome,'letras')
print('o primero nome tem ', pnome,'letras')
'''
'''
from random import randint
n1 = str(randint(1, 9999))
print('numero analisado :{}'.format(n1))
print('unidade :{}'.format(n1[3]))
print('dezena :{}'.format(n1[2]))
print('centena :{}'.format(n1[1]))
print('milhar :{}'.format(n1[0]))
'''
'''
cidade = input('escreva uma cidade')
print(cidade[:5] == 'santo')
'''
'''
nome = input('qual o seu nome ?').strip()
print('o teu nome tem silva? {}'.format('silva' in nome))
'''
'''
nome = input('digite o seu nome completo')
print(' a letra "a" aparece {} vezes no nome'.format(nome.count('a')))
'''
'''
n = input('digite o seu nome completo:').strip()
nome = n.split()
print('muito prazer em te conhecer! :)')
print('seu primeiro nome e: {}'.format(nome[0]))
print('seu ultimo nome e: {}'.format(nome[len(nome)-1]))
'''
'''
file = open("file.txt", "w")
info = "elias gonzalez castillo guerreiro penisga"
file.write(info)
file.close()
'''
'''
file = open('file.txt', 'r')
info = file.read()
print('nome:', info)
file.close()
'''









