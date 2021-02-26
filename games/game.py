import random
import copy

def print_m(M): #responsavel por printar as matrizes
	m = ''
	for row in M:
	    for item in row:
	        m += str(item)+' '
	    m += '\n'

	print(m)

def randomMatriz(): #cria as matrizes iniciais do jogo
	M = [[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]
	maskM = [['*','*','*','*'],['*','*','*','*'],['*','*','*','*'],['*','*','*','*']]
	maskMatrix = [['*','*','*','*'],['*','*','*','*'],['*','*','*','*'],['*','*','*','*']]
	random.shuffle(M)
	for i in range(4):
		random.shuffle(M[i])
	return M, maskM, maskMatrix

# randomMatriz()

def unmaskMatrix(pos,M, maskMatrix): #responsavel por transformar o * por um numero na pos certa
	x = pos[0]
	y = pos[1]

	value = M[x][y]
	maskMatrix[x][y] = str(value)

	return maskMatrix.copy(), value

def checkMask(maskMatrix): #check se tds as casas ja foram escolhidas e jogo terminou
	done = True
	for row in maskMatrix:
		done = False if '*' in row else True

	return done

def formatPos(pos): #fornata o type str que chega no input para list
	pos = pos.replace('[','')
	pos = pos.replace(']','')
	pos = pos.split(',')
	pos[0] = int(pos[0])
	pos[1] = int(pos[1])

	return pos

def userConection(M, maskMatrix, key, savePos = []): #responsavel or estabelecer a comunidação com o usuario
	pos = input('Escolha a {} posição [x,y]: '.format(key))
	pos = formatPos(pos)

	if savePos != []: 
		while pos in savePos: #enquanto a posição escolhida for igual a alguma daquelas que ja forem escolhidas
			pos = input('Posição inválida ou já escolhida. Escolha a {} posição [x,y]: '.format(key))
			pos = formatPos(pos)

	while not ((pos[0] >= 0 and pos[0] <= len(M)) and (pos[1] >= 0 and pos[1] <= len(M))) : #enquanto a posição escolhida não estiver dentro da matriz
		pos = input('Posição inválida. Escolha a {} posição [x,y]: '.format(key))
		pos = formatPos(pos)

	maskMatrix, value = unmaskMatrix(pos, M, maskMatrix)
	

	return maskMatrix, value, pos

def start():
	M, maskM, maskMatrix= randomMatriz()
	value1, value2, jogadas, savePos = 0, 0, 0, []
	while True: #loop infinito

		if jogadas % 2 == 0 or jogadas == 0:

			print_m(maskMatrix)
			maskMatrix, value, pos = userConection(M, maskMatrix, 'primeira', savePos)
			value1 = value
			savePos.append(pos)
			jogadas += 1

			print_m(maskMatrix)

		elif jogadas % 2 != 0 or jogadas == 1:

			maskMatrix, value, pos = userConection(M, maskMatrix, 'segunda', savePos)
			jogadas += 1
			value2 = value
			
			print_m(maskMatrix)

			if value1 == value2:
				maskM = copy.deepcopy(maskMatrix)
				savePos.append(pos)
				print('Parabéns, você acertou!','\n')
				if checkMask(maskMatrix):
					print('Parabéns, Você conseguiu descobrir todas as cadas em {} jogadas'.format(jogadas))
					break
			elif value1 != value2:
				maskMatrix = copy.deepcopy(maskM)
				savePos.pop()
				print('Você errou... tente de novo.','\n')


start()			

