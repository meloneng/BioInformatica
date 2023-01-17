# Bibliotecas #
import numpy as np
import re
# ----------------------------------- #
arquivo = open('input.txt', 'r')
leitura = arquivo.read()
sequencia = re.findall('[A-Z]+', leitura)

S1 = sequencia[1]
S2 = sequencia[0]

tamS1 = len(S1)
tamS2 = len(S2)

# caracteres diferentes #
mismatch = -1 
# caracteres iguais #
match = 2 
# ausencia #
gap = -3

# Inicialização da matriz de valores #
A = np.zeros((len(S2) + 1, len(S1) + 1)) # Na matriz A[i][j] podemos percorrer selecionando e calculando os valores anteriores com os atuais da matriz para chegarmos ao resultado no canto superior e entao iniciar o backtracing #

# Percorrendo a linha e coluna 1 com valores de gap #
for i, linha in enumerate(A):
    for j, elemento in enumerate(linha):
        if (i == 0 and j != 0):
            A[i][j] = A[i][j - 1] + gap
        if (i != 0 and j == 0):
            A[i][j] = A[i - 1][j] + gap

# Percorrendo as linhas e colunas restantes para formar a matriz de valores, usando os condicionais de igualdade para match e diferente para mismatch #
for i, linha in enumerate(A):
    for j, elemento in enumerate(linha):
        if (i == 0 or j == 0): continue # aqui ja temos os gaps portanto devemos continuar para atribuir os matchs e mismatchs #

        if(S2[i - 1] == S1[j - 1]): # se letra da linha for igual a letra da coluna #
            score = match
        else: # caso não sejam iguais atribuimos mismatch #
            score = mismatch
        diagonal = A[i - 1][j - 1] + score
        vertical = A[i - 1][j] + gap
        horizontal = A[i][j - 1] + gap
        A[i][j] = max(diagonal, vertical, horizontal)
        
sizeLinha = len(A) - 1
sizeColuna = len(A[0]) - 1

strRes1 = ""
strRes2 = ""

# Traceback sendo executado e testado para saber por qual caminho veio #
while sizeLinha >= 1:
  if(S1[sizeColuna - 1] == S2[sizeLinha - 1]):
      strRes1 += S1[sizeColuna - 1]
      strRes2 += S1[sizeColuna - 1]
      sizeLinha -= 1
      sizeColuna -= 1
  else:
      diagonal = A[sizeLinha - 1][sizeColuna - 1]
      horizontal = A[sizeLinha][sizeColuna - 1]
      vertical = A[sizeLinha - 1][sizeColuna]
        
      if(diagonal >= horizontal and diagonal >= vertical):
        strRes1 += S2[sizeLinha - 1]
        strRes2 += S1[sizeColuna - 1]
        sizeLinha -= 1
        sizeColuna -= 1

      elif(horizontal >= diagonal and horizontal >= vertical):
        strRes1 += "-"
        strRes2 += S1[sizeColuna - 1]

        sizeColuna -= 1
      elif(vertical >= diagonal and vertical >= horizontal):
        strRes1 += S2[sizeLinha - 1]
        strRes2 += "-"

        sizeLinha -= 1
if (sizeLinha == 0 and sizeColuna > sizeLinha):
    strRes1 += "-"
    strRes2 += S1[sizeLinha]
    
        
strRes1 = strRes1[::-1]
strRes2 = strRes2[::-1]

print('Alinhamento: ')
print('Sequencia 1: ', strRes1)
print('Sequencia 2: ', strRes2)


arquivo = open('output.txt','w')
arquivo.write(str(strRes1) + '\n')
arquivo.write(str(strRes2) + '\n')
arquivo.write('Score: ' + str(A[len(A) - 1][len(A[0]) - 1]) + '\n')
arquivo.write('Gap: ' + str(gap) + '\n')
arquivo.write('Match: ' + str(match) + '\n')
arquivo.write('Mismatch: ' + str(mismatch) + '\n')
arquivo.close()

print('score: ', A[len(A) - 1][len(A[0]) - 1])