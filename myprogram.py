# pisze program obliczania adresów sieci
import math
def binary (st):
  bin = ''
  dec = int(st)
  while dec >= 1:
    if dec % 2:
      bin = '1' + bin
    else:
      bin = '0' + bin
    dec = dec // 2 # liczy liczbę całkowitą
  while len(bin) < 8:
    bin = '0' + bin
  return bin

def decimal (st):
  n = 0
  i = 1
  bi = list(st)
  while len(bi):
    n += (int(bi[-1]) * i)
    del bi[-1]
    i *= 2
  return n

def listabin(lista):
  listab = []
  for i in (lista):
    listab.append(binary(i))
  return listab

def listadec(lista):
  listad = []
  for i in (lista):
    listad.append(str(decimal(i)))
  return listad

def listadecadd(lista1, lista2):
  listar = []
  for i in range(len(lista1)):
    listar.append(str( int(lista1[i]) + int(lista2[i]) ))
  return listar

def listamask(m):
  bin = ''
  for i in range(m):
    bin += '1'
  while len(bin) < 32:
    bin += '0'
  return [bin[0:8], bin[8:16], bin[16:24], bin[24:]]

def lista_and(l1, l2):
  lista1 = '.'.join(l1)
  lista2 = '.'.join(l2)
  r = ''
  n = len(lista1)
  for i in range(n):
    if lista1[i] == '.': r += '.'
    else:
      if lista1[i] == '1' and lista2[i] == '1': 
        r += '1'
      else: r += '0'
  return r.split('.')

def lista_not(lista):
  lista1 = '.'.join(lista)
  r = ''
  n = len(lista1)
  for i in range(n):
    if lista1[i] == '.': r += '.'
    else:
      if lista1[i] == '1': r += '0'
      else: r += '1'
  return r.split('.')

def lista_plus(li, n):
  lista = li
  i = len(lista) - 1
  lista[i] = str ( int(lista[i]) + n )
  return lista

print("%s: " % 'podaj adres IP', end='')
#s = input()
print('\n')
print("%s: " % 'podaj maskę podsieci (w postaci skróconej, czyli /n): /', end='')
#m = input()
print('\n')


# s = '192.168.1.145'
# m = 25
s = '172.16.160.200'
m = 18

m = int(m)

import sys
if len(sys.argv) > 1: 
  s = sys.argv[1]
  print ("%s" % sys.argv[1])
  

if len(sys.argv) > 2: 
  m = int (sys.argv[2])
  print ("%s" % sys.argv[1])

print('adres IP: ', s)
print('maska podsieci: ', m)
lista = s.split('.')

listab = listabin(lista)
listam = listamask(m)
listaw = lista_and(listab,listam)
listad = listadec(listaw)
listamnot = lista_not(listam)
listamdnot = listadec(listamnot)
listabroad = listadecadd(listad,listamdnot)

print ("adres IP                      : %s" % '.'.join(lista))
print ("adres IP binarnie             : %s" % '.'.join(listab))
print ("maska podsieci                : %s" % '.'.join(listam))
print ("maska podsieci dziesiętnie    : %s" % '.'.join(listadec(listam)))

print ("obliczę adres sieci NETWORK tworząc koniunkcję:")
print ("----------- adresu IP binarnie: %s" % '.'.join(listab))
print ("------ maski podsieci binarnie: %s" % '.'.join(listam))


print ("adres sieci                   : %s" % '.'.join(listaw))
print ("adres sieci dziesiętnie       : %s" % '.'.join(listad))
print ("negacja maski                 : %s" % '.'.join(listamnot))
print ("negacja maski dziesiętnie     : %s" % '.'.join(listamdnot))
print ("obliczę adres rozgłoszeniowy BROADCASTING dodając:")
print ("------ adres sieci dziesietnie: %s" % '.'.join(listad))
print ("---- negacja maski dziesiętnie: %s" % '.'.join(listamdnot))

print ("adres rozgłoszeniowy sieci    : %s" % '.'.join(listabroad))
print ("w sieci może pracować maksymalnie hostów: %d" % (math.pow(2,32-m) - 2))
print ("adres pierwszego hosta        : %s (dodałem 1 do adresu sieci)" % '.'.join(lista_plus(listad,1)))
print ("adres ostatniego hosta        : %s (odjąłem 1 od adresu rozgłoszeniowego)" % '.'.join(lista_plus(listabroad,-1)))

print ("Press Enter\n")
input()
