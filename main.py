# Programa "Sistema para economizar de mais de 8000 dolls"
# Caicó City- Programação
# Made by Sir Marcos Vinícius Naturalista de Bar
# Início:

print('\n                     Sistema para economizar dinheiro\n')




from time import sleep
import pickle
from os import system








try:
  dArq=open("div.dat", "rb")
  saldo=pickle.load(dArq)
  dArq.close()
except IOError or FileNotFoundError:
  print("Não há saldo nem dívida.")
  saldo=0
  dArq=open('div.dat', 'wb')
  pickle.dump(saldo, dArq)
  dArq.close()








sec=int(input('\n \nEscolha a seção de destino:\n1- Movimentar grana\n2- Visualizar economias\n0- Fechar o programa\n  --> '))
mov, vis, fec = 1, 2, 0
condi=[
  mov,
  vis,
  fec
]
while sec!=0:
  conta=0
  while sec not in condi and conta!=7:
    conta+=1
    sec=int(input('\n \nEscolha uma seção válida de destino:\n1- Movimentar grana\n2- Visualizar economias\n0- Fechar o sistema\n  -->  '))
  if conta==7:
    print('\nTentativas excedidas. O programa será finalizado.')
    break
  if sec==condi[0]:
    val=float(input('\nAgora insira o valor a ser depositado/usado.\nPara valor usado, ponha o Menos("-") antes.\nE para centavos, ponha o Ponto no lugar da vírgula (".")\n  Ex.: pra usar R$ 54,85  escreva -54.85\n  Digite o valor:  '))
    try:
      saldo+=val
    except:
      saldo=float(0)
      saldo+=val
    print('\n \nOperação realizada com sucesso!')
    dArq= open("div.dat", "wb")
    pickle.dump(saldo, dArq)
    dArq.close()
  elif sec==condi[1]:
    print('\n \n \nSaldo: R$ %0.2f'%(saldo))
    
  sec=int(input('\n \nEscolha uma seção de destino:\n1- Movimentar grana\n2- Visualizar economias\n0- Fechar o sistema\n  -->  '))
  


dArq= open("div.dat", "wb")
pickle.dump(saldo, dArq)
dArq.close()


print('\n \n \n \nFim do programa !')