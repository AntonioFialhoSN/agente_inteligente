import random
import time


def linha():
    print("-"*25)

def menu(lista):
    for x in range(0, len(lista)):
        print(f"{x+1} -> {lista[x]}".center(25))
    valor = int(input("Escolha uma opcao: "))
    return valor

def campo(valor):
    from random import randint
    ambiente = []
    for y in range(0, (valor + 2)):
        linha = ""
        for x in range(0, (valor + 2)):
            if(x == 0 and y == 0):
                linha = linha + "|<w>|"
            elif randint(1, 3) == 2:
                linha = linha + "|▒▒▒|"
            else:
                linha = linha + "|   |"
        ambiente.append(linha)
    for x in range(0, len(ambiente)):
        print(ambiente[x])
    return ambiente

def up_move(up, x, field):
    campo = field
    if up != 0:
        for c in range(0, len(field)):
            if (up-1) == int(c):
                linha = field[c]
                linha1 = field[c+1]
                nova_linha = linha[:x]+'|<w>|'+linha[x+5:]
                linha_anterior = linha1[:x]+'|   |'+linha1[x+5:]
                linha_retirada = campo[c]
                linha_anterior_retirada = campo[c+1]
                campo.remove(linha_anterior_retirada)
                campo.remove(linha_retirada)
                campo.insert(c, nova_linha)
                campo.insert(c+1, linha_anterior)
                return campo

def down_move (y, x, field):
    campo = field
    if y != len(campo):
        for c in range(0, len(field)):
            if (y + 1) == int(c):
                linha1 = field[c - 1]
                linha = field[c]
                nova_linha = linha[:x] + '|<w>|' + linha[x + 5:]
                linha_anterior = linha1[:x] + '|   |' + linha1[x + 5:]
                linha_anterior_retirada = campo[c - 1]
                linha_retirada = campo[c]
                campo.remove(linha_anterior_retirada)
                campo.remove(linha_retirada)
                campo.insert(c - 1, linha_anterior)
                campo.insert(c, nova_linha)
                return campo

def rigth_move(y, x, field):
    campo = field
    linha = campo[y]
    nova_linha = linha[:x]+'|   |'+'|<w>|'+linha[x+10:]
    campo.remove(linha)
    campo.insert(y,nova_linha)
    return campo

def left_move(y, x, field):
    campo = field
    linha = campo[y]
    nova_linha = linha[:x-5] + '|<w>|' + '|   |' + linha[x+5:]
    campo.remove(linha)
    campo.insert(y, nova_linha)
    return campo

def posy(field):
    for c in range(0, len(field)):
        pos = field[c].find("|<w>|")
        if (int(pos)) != -1:
            y = c
            return y

def posx(field):
    for c in range(0, len(field)):
        pos = field[c].find("|<w>|")
        if (int(pos)) != -1:
            x = pos
            return x

def escolha(valor, y, x, c):
    if valor == 1:
        novo_campo = up_move(y, x, c)
        for x in range(0, len(novo_campo)):
            print(novo_campo[x])
        return novo_campo
    elif valor == 2:
        novo_campo = down_move(y, x, c)
        for x in range(0, len(novo_campo)):
            print(novo_campo[x])
        return novo_campo
    elif valor == 3:
        novo_campo = rigth_move(y, x, c)
        for x in range(0, len(novo_campo)):
            print(novo_campo[x])
        return novo_campo
    else:
        novo_campo = left_move(y, x, c)
        for x in range(0, len(novo_campo)):
            print(novo_campo[x])
        return novo_campo

def sensor(x, y, campo):
    '''
    a = esquerda
    c = direita
    b = cima
    d = baixo

    ab = cima-esquerda
    ac = baixo-esquerda
    bc = cima-direita
    cd = baixo-direita
    '''
    if x == 0 and y == 0:
        ab = '//L'
        ac = '//L'
        bc = '//L'
        a = '//L'
        b = '//L'
        c = campo[y][x+5:x+10]
        d = campo[y+1][x:x+5]
        cd = campo[y+1][x+5:x+10]
    elif x == 0 and y+1 == len(campo):
        a = '//L'
        ab = '//L'
        ac = '//L'
        d = '//L'
        cd = '//L'
        c = campo[y][x+5:x+10]
        b = campo[y-1][x:x+5]
        bc = campo[y-1][x+5:x+10]
    elif x+5 == len(campo[y]) and y == 0:
        ab = '//L'
        bc = '//L'
        b = '//L'
        c = '//L'
        cd = '//L'
        a = campo[y][x-5:x]
        ac = campo[y+1][x-5:x]
        d = campo[y+1][x:x+5]
    elif x+5 == len(campo[y]) and y+1 == len(campo):
        bc = '//L'
        c = '//L'
        cd = '//L'
        ac = '//L'
        d = '//L'
        b = campo[y-1][x:x+5]
        a = campo[y][x-5:x]
        ab = campo[y-1][x-5:x]
    else:
        if x == 0 and y+1 != len(campo) and y != 0:
            ab = '//L'
            ac = '//L'
            a = '//L'
            bc = campo[y-1][x+5:x+10]
            b = campo[y-1][x:x+5]
            c = campo[y][x+5:x+10]
            d = campo[y+1][x:x+5]
            cd = campo[y+1][x+5:x+10]
        elif x+5 == len(campo[y]) and y+1 != len(campo) and y != 0:
            bc = '//L'
            c = '//L'
            cd = '//L'
            ac = campo[y+1][x-5:x]
            d = campo[y+1][x:x+5]
            b = campo[y-1][x:x + 5]
            a = campo[y][x-5:x]
            ab = campo[y-1][x-5:x]
        elif y == 0 and x+5 != len(campo[y]) and x != 0:
            ab = '//L'
            bc = '//L'
            b = '//L'
            c = campo[y][x+5:x+10]
            cd = campo[y+1][x+5:x+10]
            a = campo[y][x - 5:x]
            ac = campo[y + 1][x - 5:x]
            d = campo[y + 1][x:x + 5]
        elif y+1 == len(campo) and x+5 != len(campo[y]) and x != 0:
            cd = '//L'
            ac = '//L'
            d = '//L'
            bc = campo[y-1][x+5:x+10]
            c = campo[y][x+5:x+10]
            b = campo[y-1][x:x+5]
            a = campo[y][x-5:x]
            ab = campo[y-1][x-5:x]
        else:
            bc = campo[y-1][x+5:x+10]
            b = campo[y-1][x:x+5]
            c = campo[y][x+5:x+10]
            d = campo[y+1][x:x+5]
            cd = campo[y+1][x+5:x+10]
            ac = campo[y+1][x-5:x]
            a = campo[y][x-5:x]
            ab = campo[y-1][x-5:x]
    print(f'\n{ab}{b}{bc}\n{a}|   |{c}\n{ac}{d}{cd}\n')
    return [a, b, c, d, ab, bc, ac, cd]

    #'''print(f'esquerda = {a}, cima ={b}, direita = {c} , Baixo ={d}')
    #print(f'cima-esquerda: {ab}, baixo-esquerda: {ac}, cima-direita: {bc}, baixo-direita: {cd}')'''

def agente_i(s, x, y, c):
    if "|▒▒▒|" in s[0:4]:
        if s[0] == "|▒▒▒|":
            return 4
        elif s[1] == "|▒▒▒|":
            return 1
        elif s[2] == "|▒▒▒|":
            return 3
        elif s[3] == "|▒▒▒|":
            return 2
        else:
            print('erro no sensor primario')
    elif "|▒▒▒|" in s[4:6]:
        return 1
    elif "|▒▒▒|" in s[6:8]:
        return 2
    else:
        if x == 0 and y == 0:
            return random.randint(2, 3)
        elif x == 0 and y+1 == len(c):
            return random.randrange(1, 4, 2)
        elif x+5 == len(c[y]) and y == 0:
            return random.randrange(2, 5, 2)
        elif x+5 == len(c[y]) and y+1 == len(c):
            return random.randrange(1, 5, 3)
        else:
            if x == 0:
                return random.randint(1, 3)
            elif y == 0:
                return random.randint(2, 4)
            elif x+5 == len(c[y]):
                return random.randrange(1, 5, 3)
            elif y+1 == len(c):
                return random.randrange(1, 4, 3)
            else:
               return random.randint(1, 4)


linha()
lista_1 = ["3x3", "4x4", "5x5", "6x6", "7x7", "8x8", "9X9"]
opc = menu(lista_1)
linha()
field = campo(opc)
while True:
    c = field
    y = posy(c)
    x = posx(c)
    valor = agente_i(sensor(x, y, c), x, y, c)
    field = escolha(valor, y, x, c)
    time.sleep(3)
    v = 0
    for x in range(0, len(c)):
        linha = c[x]
        if '|▒▒▒|' not in linha:
            v += 1
    if v == len(c):
        print('tudo limpo')
        break